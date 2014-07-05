# -*- coding: utf-8 -*-

"""
Module implementing Warning.
"""

from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_Warning import Ui_Warning

class Warning(QDialog, Ui_Warning):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.detail=""
    
    @pyqtSignature("")
    def on_pushButton_clicked(self):
        self.label_detail.setText(self.detail)
    
    @pyqtSignature("")
    def on_pushButton_2_clicked(self):
        self.done(0)
