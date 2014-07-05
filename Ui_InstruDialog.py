# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InstruDialog.ui'
#
# Created: Mon Jun 09 12:35:38 2014
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

class Ui_InstruDialog(object):
    def setupUi(self, InstruDialog):
        InstruDialog.setObjectName(_fromUtf8("InstruDialog"))
        InstruDialog.resize(433, 366)
        self.gridLayout = QtGui.QGridLayout(InstruDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pbOK = QtGui.QPushButton(InstruDialog)
        self.pbOK.setObjectName(_fromUtf8("pbOK"))
        self.horizontalLayout.addWidget(self.pbOK)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pbCancel = QtGui.QPushButton(InstruDialog)
        self.pbCancel.setObjectName(_fromUtf8("pbCancel"))
        self.horizontalLayout.addWidget(self.pbCancel)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 1)
        self.splitter_4 = QtGui.QSplitter(InstruDialog)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName(_fromUtf8("splitter_4"))
        self.label = QtGui.QLabel(self.splitter_4)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_6 = QtGui.QLabel(self.splitter_4)
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.splitter_4, 0, 0, 1, 1)
        self.splitter = QtGui.QSplitter(InstruDialog)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.listWidgetA = QtGui.QListWidget(self.splitter)
        self.listWidgetA.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.listWidgetA.setProperty("showDropIndicator", True)
        self.listWidgetA.setObjectName(_fromUtf8("listWidgetA"))
        self.listWidgetB = QtGui.QListWidget(self.splitter)
        self.listWidgetB.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidgetB.setObjectName(_fromUtf8("listWidgetB"))
        self.gridLayout.addWidget(self.splitter, 1, 0, 1, 1)
        self.splitter_2 = QtGui.QSplitter(InstruDialog)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.label_3 = QtGui.QLabel(self.splitter_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEditInstru = QtGui.QLineEdit(self.splitter_2)
        self.lineEditInstru.setObjectName(_fromUtf8("lineEditInstru"))
        self.label_4 = QtGui.QLabel(self.splitter_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEditTable = QtGui.QLineEdit(self.splitter_2)
        self.lineEditTable.setObjectName(_fromUtf8("lineEditTable"))
        self.gridLayout.addWidget(self.splitter_2, 3, 0, 1, 1)
        self.splitter_3 = QtGui.QSplitter(InstruDialog)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.label_2 = QtGui.QLabel(self.splitter_3)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_5 = QtGui.QLabel(self.splitter_3)
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.splitter_3, 2, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 4, 0, 1, 1)

        self.retranslateUi(InstruDialog)
        QtCore.QMetaObject.connectSlotsByName(InstruDialog)

    def retranslateUi(self, InstruDialog):
        InstruDialog.setWindowTitle(_translate("InstruDialog", "仪器管理", None))
        self.pbOK.setText(_translate("InstruDialog", "确定", None))
        self.pbCancel.setText(_translate("InstruDialog", "取消", None))
        self.label.setText(_translate("InstruDialog", "当前仪器表", None))
        self.label_3.setText(_translate("InstruDialog", "仪器名", None))
        self.label_4.setText(_translate("InstruDialog", "表名", None))
        self.label_2.setText(_translate("InstruDialog", "新增仪器表", None))

