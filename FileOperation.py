# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QDialog
#import sip
#sip.setapi('QString', 2)#pyQt库中QString库的第二版var2
try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

class FilesOpera(QDialog):
	def __init__(self, parent = None,caption=u"文件操作"):
		QDialog.__init__(self, parent)
		self.caption=caption

	def FilesImport(self):
		options = QtGui.QFileDialog.Options()
		files = QtGui.QFileDialog.getOpenFileNames(self,
		unicode(self.caption).encode("utf-8").decode("utf-8"), unicode("").encode("utf-8"),
		unicode("All Files (*);;Text Files (*.txt)").encode("utf-8"),unicode("").encode("utf-8"), options)
		return files
	def FolderImport(self):
		options=QtGui.QFileDialog.Options()
		folder = QtGui.QFileDialog.getExistingDirectory(self,
		unicode(self.caption).encode("utf-8").decode("utf-8"), unicode("").encode("utf-8"), options)
		return folder

