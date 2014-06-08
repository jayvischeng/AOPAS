# -*- coding: utf-8 -*-

"""
Module implementing Delete.
"""
import sys
sys.path.append("F:\EricPython2")
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_Delete import Ui_Dialog

class Delete(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.conninfo=parent.ms
        self.sqlstr="delete from "+unicode(parent.tablename).encode("utf-8").decode("utf-8")+parent.sqlstr_condition+parent.sqlstrtail
    
    @pyqtSignature("")
    def on_pbOK_clicked(self):
        print self.sqlstr
        if self.conninfo.GetConnect()==True:
            self.conninfo.ExecuteDelete(self.sqlstr)
            print self.conninfo.title
            self.done(0)
    
    @pyqtSignature("")
    def on_pbQuit_clicked(self):
        self.done(0)
