# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Delete.ui'
#
# Created: Sun Jun 15 17:45:48 2014
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
        Dialog.resize(230, 87)
        Dialog.setMinimumSize(QtCore.QSize(230, 75))
        Dialog.setMaximumSize(QtCore.QSize(242, 87))
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter = QtGui.QSplitter(Dialog)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.pushButton_3 = QtGui.QPushButton(self.splitter)
        self.pushButton_3.setStyleSheet(_fromUtf8("border-image: url(:/ProjectImages/stop_2.png);"))
        self.pushButton_3.setText(_fromUtf8(""))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label = QtGui.QLabel(self.splitter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pbOK = QtGui.QPushButton(Dialog)
        self.pbOK.setObjectName(_fromUtf8("pbOK"))
        self.horizontalLayout.addWidget(self.pbOK)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pbQuit = QtGui.QPushButton(Dialog)
        self.pbQuit.setObjectName(_fromUtf8("pbQuit"))
        self.horizontalLayout.addWidget(self.pbQuit)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", " 你确定进行删除操作吗？", None))
        self.pbOK.setText(_translate("Dialog", "确定", None))
        self.pbQuit.setText(_translate("Dialog", "取消", None))

import Image_rc
