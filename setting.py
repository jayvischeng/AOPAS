# -*- coding: utf-8 -*-

"""
Module implementing Setting.
"""

from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_setting import Ui_Setting


class Setting(QDialog, Ui_Setting):
	"""
	Class documentation goes here.
	"""

	def __init__(self, parent=None):
		"""
		Constructor
		"""
		QDialog.__init__(self, parent)
		self.setupUi(self)
		self.ip = parent.ip
		self.host = parent.host

		self.db = parent.db
		self.user = parent.user
		self.pwd = parent.pwd
		self.settinglineEdit0.setText(self.ip)


		self.settinglineEdit1.setText(self.host)
		self.settinglineEdit2.setText(self.db)
		self.settinglineEdit3.setText(self.user)
		self.settinglineEdit4.setText(self.pwd)
		# self.settinglineEdit4.text()=self.pwd
	@pyqtSignature("")
	def on_pushButton_clicked(self):
		self.ip = self.settinglineEdit0.text()
		self.host = self.settinglineEdit1.text()
		self.db = self.settinglineEdit2.text()
		self.user = self.settinglineEdit3.text()
		self.pwd = self.settinglineEdit4.text()
		self.done(0)


	@pyqtSignature("")
	def on_pushButton_2_clicked(self):
		self.settinglineEdit0.setText("")
		self.settinglineEdit1.setText("")
		self.settinglineEdit2.setText("")
		self.settinglineEdit3.setText("")
		self.settinglineEdit4.setText("")
