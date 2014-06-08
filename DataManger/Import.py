# -*- coding: utf-8 -*-

"""
Module implementing Import.
"""
import sys

sys.path.append("F:\EricPython2")
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature
from FileOperation import *
from DataManger.Ui_Import import Ui_Import
from Warning import *
import re
import time
import datetime

sys.path.append("F:\EricPython2")


class Import(QDialog, Ui_Import):
	"""
	Class documentation goes here.
	"""

	def __init__(self, parent=None):
		"""
		Constructor
		"""
		QDialog.__init__(self, parent)
		self.setupUi(self)
		self.conninfo = parent.ms
		self.folder = []
		self.files = []
		try:
			self.comboBox.insertItems(0, self.conninfo.title)
		except:
			pass
		#----------------------------------------------------------------------------------------------#

	@pyqtSignature("")
	def on_toolButtonFolder_clicked(self):
		self.folder = []
		myF = FilesOpera()
		self.folder = myF.FolderImport()
		self.lineEditFolder.setText(self.folder)

	@pyqtSignature("")
	def on_toolButtonFiles_clicked(self):
		self.files = []
		self.filepath = []
		myF = FilesOpera()
		self.filepath = myF.FilesImport()
		tempfiles = []
		try:
			for tab in range(len(self.filepath)):
				fullpath = self.filepath[tab]
				tempfiles = fullpath.split("\\")
				self.files.append(str(tempfiles[len(tempfiles) - 1]))
				self.lineEditFiles.insert(str(tempfiles[len(tempfiles) - 1]) + '  ')
			self.FileNameFormat.insert(str(tempfiles[len(tempfiles) - 1]))
		except:
			pass

	@pyqtSignature("bool")
	def on_isHaveInfo_clicked(self, checked):
		if checked == True:
			self.FileNameFormat.setEnabled(True)
			self.index1.setEnabled(True)
			self.index2.setEnabled(True)
		else:
			self.FileNameFormat.setEnabled(False)
			self.index1.setEnabled(False)
			self.index2.setEnabled(False)

	@pyqtSignature("")
	def on_pbImport_clicked(self):
		self.idcount = 0
		#other=" "
		self.progressBar.setValue(0)
		if len(self.files) != 0 and len(self.folder) == 0:

			self.progressBar.setRange(0, len(self.files))
			self.conninfo.GetConnect()
			for tab1 in range(len(self.filepath)):
				f = open(unicode(self.filepath[tab1]).encode("utf-8").decode("utf-8"))
				sqldatas = []
				str_file = f.readlines()
				fields = self.conninfo.title
				#扫描每个文件的第一列，判断是否有时间列和日期列
				line_list = re.split(r"\t *|,| *", str_file[0].strip())
				dateIndex = -1
				timeIndex = -1
				for tab2 in range(len(line_list)):
					if line_list[tab2].find('-') == 2:
						dateIndex = tab2
					elif line_list[tab2].find(':') == 2:
						timeIndex = tab2

				for tab3 in range(len(str_file)):
					str_line = re.split(r"\t *|,| *", str_file[tab3].strip())
					if dateIndex != -1:#有日期列
						(year, month, day) = str_line[dateIndex].split('-')
					if self.isHaveInfo.isChecked():#无日期列，进行手动指定
						for tab4 in range(self.listWidget.count()):
							tempstr = unicode(self.listWidget.item(tab4).text()).encode("utf-8")
							templist = tempstr.strip().split("   ")
							#print templist
							if templist[0] == "Year":

								year = float(self.files[tab1][int(templist[1]) - 1:int(templist[2])])
							elif templist[0] == "Month":
								month = float(self.files[tab1][int(templist[1]) - 1:int(templist[2])])
							elif templist[0] == "Day":
								day = float(self.files[tab1][int(templist[1]) - 1:int(templist[2])])
							elif templist[0] == "Other":
								other = str(self.files[tab1][int(templist[1]) - 1:int(templist[2])])
					else:
						pass
					if timeIndex != -1:#有时间列
						(hour, minute, second) = str_line[timeIndex].split(':')

					self.idcount = self.idcount + 1
					datas = []
					datas.append(int(self.idcount))
					if int(year)<50:
						year=int(year)+2000
					else:
						year=int(year)+1900
					datas.append(float(year))
					datas.append(float(month))
					datas.append(float(day))

					datas.append(float(hour))
					datas.append(float(minute))
					datas.append(float(second))

					if dateIndex == -1:#无日期列
						tempdate = datetime.date(int(year), int(month), int(day)).isoformat()
						datas.append(tempdate)
						print "AAAAAAAAAAAAAAAAAAAAAAAa"
					#有日期列
					for tab in range(len(str_line)):
						print str_line[tab]
						if str_line[tab].count('-')==2:
							datas.append(datetime.date(int(year), int(month), int(day)).isoformat())
						elif ':' in str_line[tab]:
							datas.append(str_line[tab])
						else:
							datas.append(float(str_line[tab]))
						#添加地点
					datas.append(unicode(self.lineEditPlace.text()).encode("utf-8").decode("utf-8"))
					#datas.append(unicode(self.files[tab1][-5]).encode("utf-8")+"m")
					if other != "":
						datas.append(other)
					print datas

					sqlstr2 = "insert into JDMCL"
					sqlfields = ','.join(fields)
					p = re.compile('|'.join(fields))
					wildcard = p.sub('?', sqlfields)
					sqlstr2 = sqlstr2 + '(' + sqlfields + ')' + ' values (' + wildcard + ')'
					sqldatas.append(datas)
				print sqlstr2
				self.cur = self.conninfo.conn.cursor()
				self.cur.executemany(sqlstr2, sqldatas)
				self.conninfo.conn.commit()
				#time.sleep(1)
				self.progressBar.setValue(tab1 + 1)
			self.conninfo.conn.close()
			#self.model.setQuery(sqlstr2)
		elif len(self.files) == 0 and len(self.folder) != 0:
			pass

	@pyqtSignature("")
	def on_pbClear_clicked(self):
		self.listWidget.clear()

	@pyqtSignature("")
	def on_pbAdd_clicked(self):
		self.listWidget.addItem(
			str(self.comboBox.currentText()) + '   ' + self.index1.text() + '   ' + self.index2.text())

	@pyqtSignature("")
	def on_pbCancel_clicked(self):
		self.done(0)
