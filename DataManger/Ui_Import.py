# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\EricPython2\DataManger\Import.ui'
#
# Created: Sat May 03 18:35:27 2014
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

class Ui_Import(object):
    def setupUi(self, Import):
        Import.setObjectName(_fromUtf8("Import"))
        Import.setWindowModality(QtCore.Qt.WindowModal)
        Import.resize(516, 521)
        Import.setMaximumSize(QtCore.QSize(1000, 1000))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/ProjectImages/arrow_left.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Import.setWindowIcon(icon)
        Import.setSizeGripEnabled(True)
        self.verticalLayout = QtGui.QVBoxLayout(Import)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(Import)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEditFolder = QtGui.QLineEdit(Import)
        self.lineEditFolder.setObjectName(_fromUtf8("lineEditFolder"))
        self.horizontalLayout.addWidget(self.lineEditFolder)
        self.toolButtonFolder = QtGui.QToolButton(Import)
        self.toolButtonFolder.setObjectName(_fromUtf8("toolButtonFolder"))
        self.horizontalLayout.addWidget(self.toolButtonFolder)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_10 = QtGui.QLabel(Import)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_7.addWidget(self.label_10)
        self.label_11 = QtGui.QLabel(Import)
        self.label_11.setText(_fromUtf8(""))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_7.addWidget(self.label_11)
        self.lineEditFiles = QtGui.QLineEdit(Import)
        self.lineEditFiles.setObjectName(_fromUtf8("lineEditFiles"))
        self.horizontalLayout_7.addWidget(self.lineEditFiles)
        self.toolButtonFiles = QtGui.QToolButton(Import)
        self.toolButtonFiles.setObjectName(_fromUtf8("toolButtonFiles"))
        self.horizontalLayout_7.addWidget(self.toolButtonFiles)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.line_2 = QtGui.QFrame(Import)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        self.line = QtGui.QFrame(Import)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.isHaveInfo = QtGui.QCheckBox(Import)
        self.isHaveInfo.setObjectName(_fromUtf8("isHaveInfo"))
        self.horizontalLayout_3.addWidget(self.isHaveInfo)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_2 = QtGui.QLabel(Import)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_5.addWidget(self.label_2)
        self.FileNameFormat = QtGui.QLineEdit(Import)
        self.FileNameFormat.setEnabled(False)
        self.FileNameFormat.setObjectName(_fromUtf8("FileNameFormat"))
        self.horizontalLayout_5.addWidget(self.FileNameFormat)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_6 = QtGui.QLabel(Import)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 2, 1, 1, 1)
        self.index1 = QtGui.QLineEdit(Import)
        self.index1.setEnabled(False)
        self.index1.setObjectName(_fromUtf8("index1"))
        self.gridLayout.addWidget(self.index1, 1, 2, 1, 1)
        self.label_5 = QtGui.QLabel(Import)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)
        self.pbClear = QtGui.QPushButton(Import)
        self.pbClear.setObjectName(_fromUtf8("pbClear"))
        self.gridLayout.addWidget(self.pbClear, 2, 6, 1, 1)
        self.pbAdd = QtGui.QPushButton(Import)
        self.pbAdd.setObjectName(_fromUtf8("pbAdd"))
        self.gridLayout.addWidget(self.pbAdd, 1, 6, 1, 1)
        self.listWidget = QtGui.QListWidget(Import)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.gridLayout.addWidget(self.listWidget, 1, 7, 2, 1)
        self.index2 = QtGui.QLineEdit(Import)
        self.index2.setEnabled(False)
        self.index2.setObjectName(_fromUtf8("index2"))
        self.gridLayout.addWidget(self.index2, 1, 4, 1, 1)
        self.label_8 = QtGui.QLabel(Import)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 1, 3, 1, 1)
        self.comboBox = QtGui.QComboBox(Import)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout.addWidget(self.comboBox, 2, 2, 1, 3)
        self.verticalLayout.addLayout(self.gridLayout)
        self.line_3 = QtGui.QFrame(Import)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout.addWidget(self.line_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(Import)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.lineEditPlace = QtGui.QLineEdit(Import)
        self.lineEditPlace.setObjectName(_fromUtf8("lineEditPlace"))
        self.horizontalLayout_4.addWidget(self.lineEditPlace)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.line_5 = QtGui.QFrame(Import)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.verticalLayout.addWidget(self.line_5)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.pbImport = QtGui.QPushButton(Import)
        self.pbImport.setObjectName(_fromUtf8("pbImport"))
        self.horizontalLayout_2.addWidget(self.pbImport)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.pbCancel = QtGui.QPushButton(Import)
        self.pbCancel.setObjectName(_fromUtf8("pbCancel"))
        self.horizontalLayout_2.addWidget(self.pbCancel)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line_4 = QtGui.QFrame(Import)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout.addWidget(self.line_4)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_7 = QtGui.QLabel(Import)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_6.addWidget(self.label_7)
        self.label_9 = QtGui.QLabel(Import)
        self.label_9.setText(_fromUtf8(""))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_6.addWidget(self.label_9)
        self.progressBar = QtGui.QProgressBar(Import)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet(_fromUtf8(""))
        self.progressBar.setMaximum(1000)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.horizontalLayout_6.addWidget(self.progressBar)
        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.retranslateUi(Import)
        QtCore.QMetaObject.connectSlotsByName(Import)

    def retranslateUi(self, Import):
        Import.setWindowTitle(_translate("Import", "数据导入", None))
        self.label.setText(_translate("Import", "导入文件夹", None))
        self.toolButtonFolder.setText(_translate("Import", "...", None))
        self.label_10.setText(_translate("Import", "导入文件", None))
        self.toolButtonFiles.setText(_translate("Import", "...", None))
        self.isHaveInfo.setText(_translate("Import", "文件名包含其他信息", None))
        self.label_2.setText(_translate("Import", "文件名格式", None))
        self.label_6.setText(_translate("Import", "列", None))
        self.label_5.setText(_translate("Import", "下标", None))
        self.pbClear.setText(_translate("Import", "清空", None))
        self.pbAdd.setText(_translate("Import", "添加", None))
        self.label_8.setText(_translate("Import", "到", None))
        self.label_3.setText(_translate("Import", "地点：", None))
        self.pbImport.setText(_translate("Import", "导入(I)", None))
        self.pbCancel.setText(_translate("Import", "取消(C)", None))
        self.label_7.setText(_translate("Import", "进度", None))

import Image_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Import = QtGui.QDialog()
    ui = Ui_Import()
    ui.setupUi(Import)
    Import.show()
    sys.exit(app.exec_())

