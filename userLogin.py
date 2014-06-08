# -*- coding: utf-8 -*-

"""
Module implementing ulogin.
"""

from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature
from sqlAccess import *
from Ui_userLogin import Ui_Dialog

class ulogin(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.user=""
        self.pwd=""
        self.limits=-1
        self.tempInstance=parent.ms
        self.flag=False

    @pyqtSignature("")
    def on_pbReset_clicked(self):
        self.userLine.setText(u"admin")
        self.pwdLine.setText(u"admin")

    
    @pyqtSignature("")
    def on_pbBack_clicked(self):
        self.done(0)
    
    @pyqtSignature("QString")
    def on_userLine_textChanged(self, p0):
        self.userLine.setText(p0)
        self.user=p0
    
    @pyqtSignature("QString")
    def on_pwdLine_textChanged(self, p0):
        self.pwdLine.setText(p0)
        self.pwd=p0
    @pyqtSignature("bool")
    def on_radioG_clicked(self, checked):
        self.limits=0
    
    @pyqtSignature("bool")
    def on_radioU_clicked(self, checked):
        self.limits=1
    
    @pyqtSignature("")
    def on_pbLogin_clicked(self):
        cur = self.tempInstance.conn.cursor()
        print type(self.user)
        self.user=unicode(self.user).decode("utf-8").encode("utf-8")
        print type(self.user)
        self.pwd=unicode(self.pwd).decode("utf-8").encode("utf-8")
        cur.execute("select * from dbo.tb_user where UserName=\'"+self.user+"\' and PassWord=\'"+self.pwd+"\' and Limits="+str(self.limits))
        result=cur.fetchall()
        if len(result)>0:
            self.flag=True
            #self.limits=result[len(result)-1]
        self.done(0)