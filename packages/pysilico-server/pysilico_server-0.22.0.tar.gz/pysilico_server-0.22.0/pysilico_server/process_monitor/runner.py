#!/usr/bin/env python

import time
import sys
import signal
import os
import subprocess
import psutil
from plico.utils.base_runner import BaseRunner
from plico.utils.decorator import override
from plico.utils.logger import Logger
from pysilico_server.utils.process_startup_helper import \
    ProcessStartUpHelper
from pysilico_server.utils.constants import Constants


class Runner(BaseRunner):

    RUNNING_MESSAGE = "Monitor of processes is running."

    def __init__(self):
        BaseRunner.__init__(self)

        self._logger = None
        self._processes = []
        self._timeToDie = False
        self._psh = ProcessStartUpHelper()

    def _determineInstalledBinaryDir(self):
        try:
            self._binFolder = self._configuration.getValue(
                Constants.PROCESS_MONITOR_CONFIG_SECTION,
                'binaries_installation_directory')
        except KeyError:
            self._binFolder = None

    def _logRunning(self):
        self._logger.notice(self.RUNNING_MESSAGE)
        sys.stdout.flush()

    def _setSignalIntHandler(self):
        signal.signal(signal.SIGINT, self._signalHandling)

    def _signalHandling(self, signalNumber, stackFrame):
        self._logger.notice("Received signal %d (%s)" %
                            (signalNumber, str(stackFrame)))
        if signalNumber == signal.SIGINT:
            self._timeToDie = True

    def _terminateAll(self):

        def on_terminate(proc):
            self._logger.notice(
                "process {} terminated with exit code {}".
                format(proc, proc.returncode))

        self._logger.notice("Terminating all subprocesses using psutil")
        self._logger.notice("My pid %d" % os.getpid())
        parent = psutil.Process(os.getpid())
        processes = parent.children(recursive=True)
        for process in processes:
            try:
                self._logger.notice(
                    "Killing pid %d %s" % (process.pid, process.cmdline()))
                process.send_signal(signal.SIGTERM)
            except Exception as e:
                self._logger.error("Failed killing process %s: %s" %
                                   (str(process), str(e)))
        _, alive = psutil.wait_procs(processes,
                                     timeout=10,
                                     callback=on_terminate)
        if alive:
            for p in alive:
                self._logger.notice(
                    "process %s survived SIGTERM; giving up" % str(p))

        self._logger.notice("terminated all")

    def _spawnController(self, name, section):
        if self._binFolder:
            cmd = [os.path.join(self._binFolder, name)]
        else:
            cmd = [name]
        cmd += [self._configuration._filename, section]
        self._logger.notice("Controller cmd is %s" % cmd)
        mirrorController = subprocess.Popen(cmd)
        self._processes.append(mirrorController)
        return mirrorController

    def _setup(self):
        self._logger = Logger.of("Process monitor runner")
        self._setSignalIntHandler()
        self._logger.notice("Creating controller processes")
        self._determineInstalledBinaryDir()
        sections = self._configuration.numberedSectionList(
            prefix=Constants.SERVER_CONFIG_SECTION_PREFIX)
        for section in sections:
            self._spawnController(Constants.SERVER_PROCESS_NAME, section)

    def _runLoop(self):
        self._logRunning()
        while self._timeToDie is False:
            time.sleep(1)
        self._terminateAll()

    @override
    def run(self):
        self._setup()
        self._runLoop()
        return os.EX_OK

    @override
    def terminate(self, signal, frame):
        self._logger.notice("Terminating..")
        self._terminateAll()
