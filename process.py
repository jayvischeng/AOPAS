# -*- coding: utf-8 -*-

"""
Module implementing Process.
"""

from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature
from PyQt4 import  QtGui
from Ui_process import Ui_Process


class Process(QDialog, Ui_Process):
	"""
	Class documentation goes here.
	"""

	def __init__(self, parent=None):
		"""
		Constructor
		"""
		QDialog.__init__(self, parent)
		self.setupUi(self)
		self.dict1 = {"求平均": "resample", "求方差": "std"}
		self.dict2 = {"resample": [u"日平均", u"月平均"],"std": [u"标准差", u"方差"]}
		#self.dict3 = {"resample": [u"日平均", u"月平均"],"std": [u"标准差", u"方差"]}
		self.combine=""
	@pyqtSignature("QString")
	def on_pcomboBox1_currentIndexChanged(self, p0):
		#for each in self.dict1.:
		A=[]
		self.pcomboBox2.clear()
		self.pcomboBox3.clear()
		A.append(self.dict1[unicode(p0).encode("utf-8")])
		self.pcomboBox2.insertItems(0,A)

	@pyqtSignature("QString")
	def on_pcomboBox2_currentIndexChanged(self, p0):
		if p0!="":
			#print unicode(p0).encode("utf-8")
			#print self.dict2[unicode(p0).encode("utf-8")]
			#self.pcomboBox2.clear()
			self.pcomboBox3.addItems(self.dict2[unicode(p0).encode("utf-8")])
	
	@pyqtSignature("QString")
	def on_pcomboBox3_currentIndexChanged(self, p0):
		pass

	@pyqtSignature("QString")
	def on_lineEdit_textChanged(self, p0):
		pass


	@pyqtSignature("")
	def on_pbuttonOK_clicked(self):
		self.combine=self.pcomboBox2.currentText()+'\\'+self.lineEdit.text()
		self.done(0)
		#print self.combine
if __name__ == "__main__":
	import sys
	import sip
	app = QtGui.QApplication(sys.argv)
	myProcess = Process()
	#ui = Ui_Process()
	#ui.setupUi(myImport)
	myProcess.exec_()
	sys.exit(app.exec_())
	#sip.setdestroyonexit(app.exec_())
