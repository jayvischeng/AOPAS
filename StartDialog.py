# -*- coding: utf-8 -*-

"""
Module implementing StartDialog.
"""

from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature
from DataManger.Import import *
from Warning import *
from InstruDialog import *
from Ui_StartDialog import Ui_StartDialog


class StartDialog(QDialog, Ui_StartDialog):
	"""
	Class documentation goes here.
	"""

	def __init__(self, parent=None):
		"""
		Constructor
		"""
		QDialog.__init__(self, parent)
		self.setupUi(self)
		self.lineEditUser.setText(parent.userName)
		role = [u"未登录", u"管理员", u"普通用户"]
		self.lineEditLimits.setText(role[parent.userLimits + 1])
		self.flag=parent.userFlag
		self.limits=parent.userLimits
		self.i=parent.dcombox_name.currentIndex()
		self.parent=parent

	@pyqtSignature("")
	def on_pbQuit_clicked(self):
		self.done(0)


	@pyqtSignature("")
	def on_pbOK_clicked(self):
		self.done(0)

	@pyqtSignature("")
	def on_pBUserManage_clicked(self):
		"""
		Slot documentation goes here.
		"""
		# TODO: not implemented yet
		raise NotImplementedError

	@pyqtSignature("")
	def on_pBProjectManage_clicked(self):
		"""
		Slot documentation goes here.
		"""
		# TODO: not implemented yet
		raise NotImplementedError

	@pyqtSignature("")
	def on_pBLogManage_clicked(self):
		"""
		Slot documentation goes here.
		"""
		# TODO: not implemented yet
		raise NotImplementedError

	@pyqtSignature("")
	def on_pBPlaceManage_clicked(self):
		"""
		Slot documentation goes here.
		"""
		# TODO: not implemented yet
		raise NotImplementedError

	@pyqtSignature("")
	def on_pBInstruManage_clicked(self):
		if self.flag==True and self.limits==0:
			instrudialog=InstruDialog(self.parent)
			instrudialog.exec_()
		else:
			war1 = Warning(self)
			war1.label_warning.setText(u"您没有登录或不具有管理员权限")
			war1.detail = u"      请确保您已经成功登录\n   并确保您的账户具有管理员权限！"
			war1.exec_()

	@pyqtSignature("")
	def on_pBPersonnelManage_clicked(self):
		"""
		Slot documentation goes here.
		"""
		# TODO: not implemented yet
		raise NotImplementedError

	@pyqtSignature("")
	def on_pBExperiment_clicked(self):
		"""
		Slot documentation goes here.
		"""
		# TODO: not implemented yet
		raise NotImplementedError

	@pyqtSignature("")
	def on_pbDataImport_clicked(self):
		if self.flag==True and self.limits==0:
			print self.i
			if self.i > 0:
				import1 = Import(self.parent)
				import1.exec_()
			else:
				war1 = Warning(self)
				war1.label_warning.setText(u"     数据库表连接失败!")
				war1.detail = u"       请检查是否选择了数据表!"
				war1.exec_()
		else:
			war1 = Warning(self)
			war1.label_warning.setText(u"您没有登录或不具有管理员权限")
			war1.detail = u"      请确保您已经成功登录\n   并确保您的账户具有管理员权限！"
			war1.exec_()

	@pyqtSignature("")
	def on_pbMainWindow_clicked(self):
		self.done(0)
