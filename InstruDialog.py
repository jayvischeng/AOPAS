# -*- coding: utf-8 -*-

"""
Module implementing InstruDialog.
"""

from PyQt4.QtGui import QDialog,QAbstractItemView
from PyQt4.QtCore import pyqtSignature

from Ui_InstruDialog import Ui_InstruDialog


class InstruDialog(QDialog, Ui_InstruDialog):
	"""
	Class documentation goes here.
	"""

	def __init__(self, parent=None):
		"""
		Constructor
		"""
		QDialog.__init__(self, parent)
		self.setupUi(self)
		self.A = parent.AList
		self.B = parent.BList
		for tab in range(len(self.A)):
			#self.A[tab]=unicode(self.A[tab]).encode("utf-8").decode("utf-8")
			#print self.A[tab]
			self.listWidgetA.insertItem(tab, self.A[tab])
		for tab in range(len(self.B)):
			self.listWidgetB.insertItem(tab, self.B[tab])

	
	@pyqtSignature("QModelIndexList")
	def on_listWidgetA_indexesMoved(self, indexes):
		pass
		#print "haha"
	
	@pyqtSignature("int")
	def on_listWidgetA_currentRowChanged(self, currentRow):
		self.listWidgetB.setCurrentRow(currentRow)
		self.listWidgetB.scrollToItem(self.listWidgetB.item(currentRow),hint=QAbstractItemView.PositionAtBottom)

	@pyqtSignature("")
	def on_pbOK_clicked(self):
		pass


	@pyqtSignature("")
	def on_pbCancel_clicked(self):
		pass

