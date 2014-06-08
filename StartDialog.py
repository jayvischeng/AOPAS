# -*- coding: utf-8 -*-

"""
Module implementing StartDialog.
"""

from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_StartDialog import Ui_StartDialog

class StartDialog(QDialog, Ui_StartDialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.lineEditUser.setText(parent.userName)
        role=[u"未登录",u"管理员",u"普通用户"]
        self.lineEditLimits.setText(role[parent.userLimits+1])