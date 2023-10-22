#############################################################################
# Code description
"""
Stacks x Easy/A Hackathon
Python Qt5 GUI for to read smart contracts for audit.
"""

# Author and version
__author__ = 'Samy Hocine'
__version__ = '0.1'

#############################################################################
#############################################################################
# To-do list

#############################################################################
#############################################################################
# Changelog

# 22/10/2023 - Version 0.1
# Stable version of the software

#############################################################################
#############################################################################
# Modules & libraries
import os
import sys
from PyQt5.QtWidgets import QApplication

#############################################################################
#############################################################################
# Location where the code is executed
__location__ = os.path.dirname(os.path.realpath(__file__))

# needed to import modules
scripts_dir = os.path.join(__location__,'scripts')
sys.path.append(scripts_dir) 

#############################################################################
#############################################################################
# Import the different scripts
from scripts.SCUI_Window import SCUI_Window
SCUI_Window.version(__version__)

from scripts.SCUI_Controller import SCUI_Controller

#############################################################################
#############################################################################
# Client code
def main():
    """Main function."""

    # Create an instance of QApplication
    PySCUI= QApplication(sys.argv)
    # Show the GUI
    view = SCUI_Window()
    view.show()
    # Create instances of the controller
    SCUI_Controller(view=view)
    # Execute the main loop
    sys.exit(PySCUI.exec_())

if __name__ == '__main__':
    main()