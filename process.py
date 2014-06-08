# -*- coding: utf-8 -*-

"""
Module implementing Process.
"""

from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_process import Ui_Process

class Process(QDialog, Ui_Process):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)

