#############################################################################
# Code description
"""Script to generate the UI window."""

#############################################################################
#############################################################################
# Modules & libraries
from PyQt5.QtWidgets import (QGroupBox,QVBoxLayout, QWidget, QGridLayout,
                             QLabel, QLineEdit, QMainWindow, QPushButton,
                             QPlainTextEdit)
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtCore import Qt
from pyqtspinner.spinner import WaitingSpinner

#############################################################################
#############################################################################
# Import the different scripts
from SCUI_Variables import Icons

#############################################################################
#############################################################################
# Create a subclass of QMainWindow to setup the GUI
class SCUI_Window(QMainWindow):
    """PyICC_Window's View (GUI)."""
    def __init__(self):
        """View initializer."""
        super().__init__()

        # Initiate variables
        global __version__
        self.ctrls = {}

        # Load icons
        self.banner = QPixmap(Icons.banner)

        # Create the display and the buttons
        self.setMainWindow()
        self.fillCtrlsDict()
        self.fillUI()

#############################################################################
    # Set the main window's properties
    def setMainWindow(self):
        """Set the main window's properties."""
        self.setWindowTitle('Clarify AI v%s' % __version__)
        # self.setFixedSize(1000,600)
        self.setFixedWidth(800)

        # Set the central widget and the general layout
        self._centralWidget = QWidget(self)
        self.generalLayout = QVBoxLayout(self._centralWidget)
        self.setCentralWidget(self._centralWidget)

        # Add the banner
        bannerLabel = QLabel()
        bannerLabel.setAlignment(Qt.AlignCenter)
        bannerLabel.setPixmap(self.banner)
        self.generalLayout.addWidget(bannerLabel)

#############################################################################
    # Create the controls
    def fillCtrlsDict(self):
        """Create and store the various controls."""
        self.ctrls['input'] = QLineEdit()

        self.ctrls['smart_contract'] = QPlainTextEdit()
        self.ctrls['smart_contract'].setReadOnly(True)
        self.ctrls['spinner_sc'] = WaitingSpinner(self, color=QColor(92, 182, 248),
                                                  lines=40, radius=15, line_width=20)

        self.ctrls['output'] = QPlainTextEdit()
        self.ctrls['output'].setReadOnly(True)
        self.ctrls['spinner_out'] = WaitingSpinner(self, color=QColor(92, 182, 248),
                                                   lines=40, radius=15, line_width=20)
        self.ctrls['display'] = QLineEdit()
        self.ctrls['display'].setReadOnly(True)

        self.ctrls['go'] = QPushButton('Go')

#############################################################################
    # Fill the UI
    def fillUI(self):
        """Populate the UI."""
        inputBox = QGroupBox('Input contract key')
        self.generalLayout.addWidget(inputBox)
        loadLayout = QGridLayout(inputBox)
        row = 0
        loadLayout.addWidget(QLabel('Contract:'),row,0)
        loadLayout.addWidget(self.ctrls['input'],row,1)
        loadLayout.addWidget(self.ctrls['go'],row,2)

        scBox = QGroupBox('Smart contract')
        self.generalLayout.addWidget(scBox)
        scLayout = QGridLayout(scBox)
        scLayout.addWidget(self.ctrls['smart_contract'],0,0)
        scLayout.addWidget(self.ctrls['spinner_sc'],0,0)

        outputBox = QGroupBox('Open AI output')
        self.generalLayout.addWidget(outputBox)
        outputLayout = QGridLayout(outputBox)
        outputLayout.addWidget(self.ctrls['output'],0,0)
        outputLayout.addWidget(self.ctrls['spinner_out'],0,0)

        displayBox = QGroupBox('Display')
        self.generalLayout.addWidget(displayBox)
        displayLayout = QVBoxLayout(displayBox)
        displayLayout.addWidget(self.ctrls['display'])

#############################################################################
    # General functions to interact with Ui elements and pass variables
    def version(ver):
        """Pass the version variable from the main script."""
        global __version__
        __version__ = ver

    def setScText(self,text):
        """Set output's text."""
        self.ctrls['smart_contract'].insertPlainText(text)

    def clearScText(self):
        """clear display's text."""
        self.ctrls['smart_contract'].clear()

    def setOutputText(self,text):
        """Set output's text."""
        self.ctrls['output'].insertPlainText(text)

    def clearOutputText(self):
        """clear display's text."""
        self.ctrls['output'].clear()

    def setDisplayText(self,text):
        """Set display's text."""
        self.ctrls['display'].setText(text)

    def enableBtns(self, state):
        self.ctrls['go'].setEnabled(state)