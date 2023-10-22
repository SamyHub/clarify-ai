#############################################################################
# Code description
"""Script to generate the UI controller."""

#############################################################################
#############################################################################
# Modules & libraries
import os
from functools import partial
from PyQt5.QtCore import QThread

#############################################################################
#############################################################################
# Import the different scripts
from SCUI_Worker import SCUI_Worker

#############################################################################
#############################################################################
# Location where the code is executed
__location__ = os.path.dirname(os.path.realpath(__file__))

#############################################################################
#############################################################################
# Create a Controller class for the GUI
class SCUI_Controller:
    """UI Controller class."""
    def __init__(self, view):
        """Controller initializer."""
        # class instances
        self._view = view

        # Initiate methods
        self.setSc = self._view.setScText
        self.clearSc = self._view.clearScText
        self.setOutput = self._view.setOutputText
        self.clearOutput = self._view.clearOutputText
        self.setDisplay = self._view.setDisplayText

        # Connect signals and slots
        self.connectSignals()

        # local variables
        self.threadRunning = False

#############################################################################
# General functions
    def openThread(self):
        self.threadRunning = True
        self.clearSc()
        self.clearOutput()
        self._view.ctrls['spinner_sc'].start()
        self._view.ctrls['spinner_out'].start()
        self.setDisplay('Thread running.')
        self.thread = QThread()
        self.worker = SCUI_Worker()
        self.worker.moveToThread(self.thread)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.finished.connect(self.threadStopped)
        self.thread.finished.connect(self._view.ctrls['spinner_sc'].stop)
        self.thread.finished.connect(self._view.ctrls['spinner_out'].stop)
        # Link the buttons
        self.thread.started.connect(partial(self._view.enableBtns, False))
        self.worker.finished.connect(partial(self._view.enableBtns, True))

    def threadStopped(self):
        self.threadRunning = False

#############################################################################
# Functions to start thread
    def getReponse(self):
        self.input = self._view.ctrls['input'].text()
        if self.input:
            try: 
                # Open the thread
                self.openThread()
                # Pass the contract ID
                self.worker.setContract(self.input)
                self.thread.started.connect(self.worker.askOpenAI)
                # Update the GUI
                self.worker.display.connect(self.setDisplay)
                self.worker.smart_contract.connect(self.setSc)
                self.worker.output.connect(self.setOutput)
                # Start the thread
                self.thread.start()
            except ValueError:
                self.setDisplay('Something went wrong in the controller!')
        else:
            self.clearSc()
            self.clearOutput()
            self.setDisplay('Please enter some text!')

#############################################################################
# connect signals
    def connectSignals(self):
        """Connect initial signals and slots."""
        self._view.ctrls['go'].clicked.connect(partial(self.getReponse))