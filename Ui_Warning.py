# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\EricPython2\Warning.ui'
#
# Created: Sat May 03 18:25:48 2014
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_Warning(object):
    def setupUi(self, Warning):
        Warning.setObjectName(_fromUtf8("Warning"))
        Warning.setWindowModality(QtCore.Qt.WindowModal)
        Warning.resize(352, 291)
        Warning.setMaximumSize(QtCore.QSize(352, 291))
        self.label = QtGui.QLabel(Warning)
        self.label.setGeometry(QtCore.QRect(110, 250, 141, 31))
        self.label.setStyleSheet(_fromUtf8("font: 75 11pt \"Calibri\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_warning = QtGui.QLabel(Warning)
        self.label_warning.setGeometry(QtCore.QRect(60, 60, 281, 41))
        self.label_warning.setStyleSheet(_fromUtf8("font: 75 12pt \"DFKai-SB\";"))
        self.label_warning.setText(_fromUtf8(""))
        self.label_warning.setObjectName(_fromUtf8("label_warning"))
        self.pushButton = QtGui.QPushButton(Warning)
        self.pushButton.setGeometry(QtCore.QRect(70, 130, 76, 24))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Warning)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 130, 81, 24))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_detail = QtGui.QLabel(Warning)
        self.label_detail.setGeometry(QtCore.QRect(30, 170, 311, 71))
        self.label_detail.setStyleSheet(_fromUtf8("font: 75 9pt \"DFKai-SB\";"))
        self.label_detail.setText(_fromUtf8(""))
        self.label_detail.setObjectName(_fromUtf8("label_detail"))

        self.retranslateUi(Warning)
        QtCore.QMetaObject.connectSlotsByName(Warning)

    def retranslateUi(self, Warning):
        Warning.setWindowTitle(_translate("Warning", "Warning", None))
        self.label.setText(_translate("Warning", "www.aiofm.ac.cn", None))
        self.pushButton.setText(_translate("Warning", "详细信息", None))
        self.pushButton_2.setText(_translate("Warning", "确定", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Warning = QtGui.QDialog()
    ui = Ui_Warning()
    ui.setupUi(Warning)
    Warning.show()
    sys.exit(app.exec_())

