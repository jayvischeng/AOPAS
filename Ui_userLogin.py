# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userLogin.ui'
#
# Created: Fri Jun 06 22:51:49 2014
#      by: PyQt4 UI code generator 4.11
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(421, 278)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/ProjectImages/user.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.pbReset = QtGui.QPushButton(Dialog)
        self.pbReset.setGeometry(QtCore.QRect(170, 150, 93, 28))
        self.pbReset.setObjectName(_fromUtf8("pbReset"))
        self.pbBack = QtGui.QPushButton(Dialog)
        self.pbBack.setGeometry(QtCore.QRect(280, 150, 93, 28))
        self.pbBack.setObjectName(_fromUtf8("pbBack"))
        self.userLine = QtGui.QLineEdit(Dialog)
        self.userLine.setGeometry(QtCore.QRect(160, 30, 131, 21))
        self.userLine.setObjectName(_fromUtf8("userLine"))
        self.pwdLine = QtGui.QLineEdit(Dialog)
        self.pwdLine.setGeometry(QtCore.QRect(160, 70, 131, 21))
        self.pwdLine.setEchoMode(QtGui.QLineEdit.Password)
        self.pwdLine.setObjectName(_fromUtf8("pwdLine"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 30, 41, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 70, 41, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(160, 200, 121, 20))
        self.label_3.setStyleSheet(_fromUtf8("font: 75 9pt \"Comic Sans MS\";"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(100, 230, 251, 20))
        self.label_4.setStyleSheet(_fromUtf8("font: 75 9pt \"Comic Sans MS\";"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.radioU = QtGui.QRadioButton(Dialog)
        self.radioU.setGeometry(QtCore.QRect(100, 110, 91, 19))
        self.radioU.setObjectName(_fromUtf8("radioU"))
        self.pbLogin = QtGui.QPushButton(Dialog)
        self.pbLogin.setGeometry(QtCore.QRect(60, 150, 93, 28))
        self.pbLogin.setObjectName(_fromUtf8("pbLogin"))
        self.radioG = QtGui.QRadioButton(Dialog)
        self.radioG.setGeometry(QtCore.QRect(230, 110, 81, 19))
        self.radioG.setObjectName(_fromUtf8("radioG"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "连接数据库", None))
        self.pbReset.setText(_translate("Dialog", "重置", None))
        self.pbBack.setText(_translate("Dialog", "返回", None))
        self.label.setText(_translate("Dialog", "账户", None))
        self.label_2.setText(_translate("Dialog", "密码", None))
        self.label_3.setText(_translate("Dialog", "     欢迎使用！", None))
        self.label_4.setText(_translate("Dialog", "www.aiofm.ac.cn 2013 Copy Right", None))
        self.radioU.setText(_translate("Dialog", "普通用户", None))
        self.pbLogin.setText(_translate("Dialog", "登陆", None))
        self.radioG.setText(_translate("Dialog", "管理员", None))

import Image_rc
