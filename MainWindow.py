# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
"""
Module implementing MainWindow.
"""

from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QDialog
from PyQt4.QtGui import QAction, QActionGroup, QMenu, QBoxLayout
from PyQt4.QtCore import pyqtSignature
from Ui_MainWindow import Ui_MainWindow
from PyQt4 import QtCore, QtGui, QtSql
from sqlAccess import *
from FileOperation import *
from Warning import *
from PyQt4.QtCore import QDate
from PyQt4.QtCore import QString
from decimal import *
from package1.mymodule1 import myfunction1
from PAA import paa
from PLR_EFP import plrefp
#from mpl_toolkits.mplot3d import axes3d
from matplotlib.backends.backend_qt4 import NavigationToolbar2QT as NavigationToolbar
#from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from userLogin import *
from DataManger.Import import *
from DataManger.Delete import *
#from Ui_uidlg import Ui_Dialog
from setting import *
from StartDialog import *
from Warning import *
from PyQt4.QtGui import *
import time
import numpy as np
import datetime
import re
import sip
import pandas
import matplotlib.pyplot as plt
from DataFrame import *
from OutLog import *
from Console import *
from FileOperation import *
from pandas import DataFrame, Index
import sys
import numpy as np
from PyQt4.QtCore import QRect, QTime
import pyodbc
import pandas.io.sql as psql
import pandas as pd
from pandas import DataFrame
#from pandas.Series import *
from pandas import Series
#from Series import *
from process import *
from Query import *
import functools
getcontext().prec = 3
try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s
from matplotlibwidget import *

class MainWindow(QMainWindow, Ui_MainWindow):
	"""
	Class documentation goes here.
	"""

	def __init__(self, parent=None):
		"""
		Constructor
		"""
		QMainWindow.__init__(self, parent)
		self.setupUi(self)


		self.console = Console(startup_message=welcome_message)
		self.console.setStyleSheet(_fromUtf8("font: 75 11pt \"微软雅黑\";\n"
											 "background-color: rgb(245, 245, 245);\n"
											 "color: rgb(0, 0, 0);\n"
											 "selection-color: rgb(255, 170, 0);"))
		self.verticalLayout_6.addWidget(self.console)
		self.console.updateNamespace({'myVar1': app, 'myVar2': 1234})



		self.openFilesPath = ""
		self.userFlag=False
		self.userName=""
		self.userLimits=-1
		self.flag2 = 1
		self.idcount = 100
		self.ip= "127.0.0.1"
		self.host = "CHENGMIN-PC\MSSQLSERVERCM"
		self.user = "sa"
		self.pwd = "111"
		self.isProcess=False
		self.db = "AOPAS_DATABASE"
		"""
		self.ip= ""
		self.host = "Local MySQL55"
		self.user = "chengmin"
		self.pwd = "chengmin123"
		"""

		#self.ms = MSSQL(host=self.ip+"\\"+self.host, user=self.user, pwd=self.pwd, db=self.db)
#

		self.tablename = ""
		self.sqlstr_condition = ""
		self.sqlstrtail = ""
#打开文件
		self.actionOpenFolder.triggered.connect(functools.partial(self.openDirectory,self.actionOpenFolder))
		self.action_f1.triggered.connect(functools.partial(self.openDirectory,self.action_f1))
		self.action_f2.triggered.connect(functools.partial(self.openDirectory,self.action_f2))
#保存文件
		self.actionSave.triggered.connect(functools.partial(self.openDirectory,self.actionSave))
		self.actionS3.triggered.connect(functools.partial(self.openDirectory,self.actionS3))
		self.actionS4.triggered.connect(functools.partial(self.openDirectory,self.actionS4))
#系统退出
		self.actionLoginOut.triggered.connect(functools.partial(self.Quit,self.actionLoginOut))
		self.actionS5.triggered.connect(functools.partial(self.Quit,self.actionS5))
#用户登录
		self.connect(self.actionD1, QtCore.SIGNAL("triggered()"),functools.partial(self.userLogin,self.actionD1))
		self.connect(self.actionLoginIn, QtCore.SIGNAL("triggered()"),functools.partial(self.userLogin,self.actionLoginIn))
#系统设置
		self.connect(self.actionSetting, QtCore.SIGNAL("triggered()"),functools.partial(self.Setting,self.actionSetting))
		self.connect(self.actionT1, QtCore.SIGNAL("triggered()"),functools.partial(self.Setting,self.actionT1))
#数据导入
		self.connect(self.actionImport, QtCore.SIGNAL("triggered()"),functools.partial(self.Import,self.actionImport))
		self.connect(self.actionD2, QtCore.SIGNAL("triggered()"),functools.partial(self.Import,self.actionD2))
#数据删除
		self.actionD3.triggered.connect(self.Delete)
#数据查询
		self.connect(self.actionDpb_Query, QtCore.SIGNAL("triggered()"),functools.partial(self.Query,self.actionDpb_Query))
		self.connect(self.actionD4, QtCore.SIGNAL("triggered()"),functools.partial(self.Query,self.actionD4))
#数据下载
		self.actionD5.triggered.connect(self.D5)
		self.customContextMenuRequested.connect(self.mainwindowRightClick)
#数据排序
		self.actionAscend.triggered.connect(functools.partial(self.Sort,self.actionAscend))
		self.actionDescend.triggered.connect(functools.partial(self.Sort,self.actionDescend))


		self.dtableView.horizontalHeader().sectionClicked.connect(self.dbsectionClicked)
		self.dtableView.horizontalHeader().sectionDoubleClicked.connect(self.dbsectionDoubleClicked)

		self.dtableView.horizontalHeader().setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.dtableView.horizontalHeader().customContextMenuRequested.connect(functools.partial(self.dbRightClicked,self.dtableView))
		#self.dtextEdit.customContextMenuRequested.connect(functools.partial(self.dbRightClicked,self.tableView))
		#self.model = QtSql.QSqlQueryModel()
		self.mplwidget.temp1=[]
		self.dcheckBoxX.checked = True
		self.dcheckBoxX.checked = True
		self.dcheckBoxX.checked = True
		self.Xindex = -1
		self.Yindex = -1
		self.Zindex = -1
		self.Xresult = []
		self.Yresult = []
		self.Zresult = []
		self.YcountA=0
		self.YcountB=0
		self.navi_toolbar = NavigationToolbar(self.mplwidget, self)
		self.a=""
		self.verticalLayout_7.addWidget(self.mplwidget)
		self.verticalLayout_7.addWidget(self.navi_toolbar)
		#        self.navi_toolbar.setBottom()

		self.ms=None
		self.dlabel_serverinfo.setText(self.dlabel_serverinfo.text() + self.host)
		self.dockWidget_calender.hide()
		self.dockWidget_compare.hide()

		self.AList = [u"近地面测量系统",u"湍流探测激光雷达",u"Airda16000低平流层风廓线雷达",u"全天空成像仪",u"大孔径闪烁仪",\
				  u"POM-02太阳辐射计",u"DTF太阳辐射计",u"PGS太阳辐射计",u"温度脉动仪",\
				  u"自动气象站,CO2传感器",u"常规气象参数测量系统(35mTower,华云技术AWS)",u"图像采集系统",u"光纤湍流测量系统",\
				  u"大气能见度仪",u"光学粒子计数器(OPC)",u"微脉冲激光雷达(MPL)",u"光纤光谱仪",\
				  u"APS3321",u"炭黑仪(AE31),烛度计(3563)",u"手持太阳辐射计",u"车载风雷达(WP3000)",\
				  u"大气相干长度仪",u"天空亮度仪"]

		self.BList = ["JDMCL","RTSL","dbo.tb_Airda16000_1","TSI880","LALS",\
				  "POM02","DTF","PGS","QHTP",\
				  "WXGMP","TOAWS","Image","FOTS",\
				  "BELFORT","OPC","MPL","MAYA2000",\
				  "APS3321","AE3563","MicrotopsII","WP3000",\
				  "DQXGCDY", "TKLDY"]
		self.tablename = unicode(self.dcombox_name.currentText()).encode("utf-8")
		self.tablenamedict = dict(zip(self.AList, self.BList))

		self.columnChooseIndex=[]
		self.actionS1.triggered.connect(self.S1)
		self.action_StartDialog.triggered.connect(self.StartDialog)
		self.labelA=0






		#self.actionE1.triggered.connect(self.textEdit.undo)
		#self.actionE2.triggered.connect(self.textEdit.redo)
		#self.actionE3.triggered.connect(self.textEdit.copy)
		#self.actionE4.triggered.connect(self.textEdit.paste)
		#self.actionE5.triggered.connect(self.textEdit.cut)

		self.actionV1.triggered.connect(self.databaseShow)
		self.actionV2.triggered.connect(self.CompareShow)
		#self.actionV3.triggered.connect(self.ControlShow)
		self.actionV4.triggered.connect(self.DetailShow)
		self.actionV5.triggered.connect(self.CalendarShow)

		self.actionP1.triggered.connect(self.P1)
		#self.actionP2.triggered.connect(self.P2)
		#self.actionP3.triggered.connect(self.P3)
		self.actionP4.triggered.connect(self.P4)
		self.actionP5.triggered.connect(self.P5)
		#self.actionP6.triggered.connect(self.P6)


		self.actionT2.triggered.connect(self.T2)

		self.actionH1.triggered.connect(self.H1)

		self.actionAbout.triggered.connect(self.About)


		#self.actionLoginIn.triggered.connect(self.userLogin)
		self.actionDataBase.triggered.connect(self.databaseShow)
		self.actionDetail.triggered.connect(self.DetailShow)
		self.actionCalender.triggered.connect(self.CalendarShow)

		self.actionControl.triggered.connect(self.ControlShow)
		self.actionMain.triggered.connect(self.Main)
		self.actionCompare.triggered.connect(self.CompareShow)

		self.actionDpb_Plot.triggered.connect(self.Plot)

		self.toolButton_print.clicked.connect(self.Print)
		#-------------------------------------------------------


		#self.mplwidget.rightMenu.exec_(QtGui.QCursor.pos())

		#self.mplwidget.contextMenuEvent(0)

		#---------------------------------------------------------
		saveout = sys.stdout
		sys.stdout = OutLog(self.dtextEdit)
		#sys.stdout=self.dtextEdit

		self.PlotMenu = QtGui.QMenu(u"绘制图形..(P)", self)
		self.L=QtGui.QAction(u"直线..(L)",self,)
		self.L.triggered.connect(functools.partial(self.Plot,self.L))
		self.S=QtGui.QAction(u"描点..(S)",self,)
		self.S.triggered.connect(functools.partial(self.Plot,self.S))
		self.SL=QtGui.QAction(u"直线+符号..(Y)",self,)
		self.SL.triggered.connect(functools.partial(self.Plot,self.SL))
		self.B=QtGui.QAction(u"条形图..(B)",self,)
		self.B.triggered.connect(functools.partial(self.Plot,self.B))
		self.C=QtGui.QAction(u"柱形图..(C)",self,)
		self.C.triggered.connect(functools.partial(self.Plot,self.C))
		self.E=QtGui.QAction(u"饼形图..(E)",self,)
		self.E.triggered.connect(functools.partial(self.Plot,self.E))
		self.PlotMenu.addAction(self.L)
		self.PlotMenu.addSeparator()
		self.PlotMenu.addAction(self.S)
		self.PlotMenu.addSeparator()
		self.PlotMenu.addAction(self.SL)
		self.PlotMenu.addSeparator()
		self.PlotMenu.addSeparator()
		self.PlotMenu.addAction(self.B)
		self.PlotMenu.addSeparator()
		self.PlotMenu.addAction(self.C)
		self.PlotMenu.addSeparator()
		self.PlotMenu.addAction(self.E)

		self.setX = QtGui.QAction(u"设为X", self)
		self.setX.triggered.connect(functools.partial(self.addXYZ,self.setX))

		self.setY = QtGui.QAction(u"设为Y", self)
		self.setY.triggered.connect(functools.partial(self.addXYZ,self.setY))

		self.setZ = QtGui.QAction(u"设为Z", self)
		self.setZ.triggered.connect(functools.partial(self.addXYZ,self.setZ))


		self.fivePJ = QtGui.QAction(u"日平均", self, triggered=self.fivePinjun)
		self.process = QtGui.QAction(u"数据处理", self, triggered=self.Process)
		self.corr = QtGui.QAction(u"相关系数", self, triggered=self.Process)

		self.statisMenu=QtGui.QMenu(u"统计...(S)", self)

		self.count=QtGui.QAction(u"计数..(非空值数)",self,)
		self.count.triggered.connect(functools.partial(self.Stastics,self.count))
		self.statisMenu.addAction(self.count)

		self.description=QtGui.QAction(u"统计信息",self,)
		self.description.triggered.connect(functools.partial(self.Stastics,self.description))
		self.statisMenu.addAction(self.description)



	#sys.stdout = self.textEdit
	#sys.stderr = OutLog( self.textEdit, sys.stderr, QtGui.QColor(255,255,0) )
	#sys.stdout=saveout


	#以下为函数实现
	#---------------------------------------------------------
	def mainwindowRightClick(self):#主窗口右键响应函数
		rightMenu = QtGui.QMenu(self)
		# 可以指定自定义对象事件
		# triggered 为右键菜单点击后的激活事件。这里slef.close调用的是系统自带的关闭事件。
		loginAction = QtGui.QAction(u"用户登录", self, triggered=self.userLogin)
		settingAction = QtGui.QAction(u"数据库设置", self, triggered=self.Setting)
		queryActionQuit = QtGui.QAction(u"关闭查询控制台", self, triggered=self.QueryShowQuit)
		quitAction = QtGui.QAction(u"退出系统", self, triggered=self.close)
		printAction = QtGui.QAction(u"打印输出", self, triggered=self.Print)
		rightMenu.addAction(loginAction)
		rightMenu.addSeparator()
		rightMenu.addAction(settingAction)
		rightMenu.addSeparator()
		rightMenu.addAction(queryActionQuit)
		rightMenu.addSeparator()
		rightMenu.addAction(quitAction)
		rightMenu.addSeparator()
		rightMenu.addAction(printAction)
		rightMenu.exec_(QtGui.QCursor.pos())
	def QueryShowQuit(self):
		print self.tabWidget_3.count()
		if self.tabWidget_3.count()>=4:
			self.tabWidget_3.removeTab(1)
		#self.tabWidget_3.insertTab(5,self.tab_5,"AAAAA")
		print "SUCCESS"
#打开文件夹路径
	def openDirectory(self,action):#打开文件路径对话框后，根据传入的action判断是打开、保存还是另存为操作
		#options = QtGui.QFileDialog.Options()
		if action==self.actionOpenFolder or action==self.action_f2:
			self.folder=FilesOpera(caption=QtCore.QString(u"打开文件夹")).FolderImport()
		elif action==self.actionSave or action==self.actionS3:
			self.folder=FilesOpera(caption=QtCore.QString(u"保存文件夹")).FolderImport()
		elif action==self.action_f1:
			self.file=FilesOpera(caption=QtCore.QString(u"打开文件")).FilesImport()
		elif action==self.actionS4:
			self.file=FilesOpera(caption=QtCore.QString(u"文件另存为")).FilesImport()
			#files = QtGui.QFileDialog.getOpenFileNames(self,
													#_fromUtf8("打开文件夹"),
											 		#_fromUtf8(self.openFilesPath),
											 		#_fromUtf8("All Files (*);;Text Files (*.txt)"), _fromUtf8(""), options)
		#if files:
			#self.openFilesPath = files[0]
		#for tab in range(len(files)):
			#fullpath = files[tab]
			#self.filenames = fullpath.split("\\")
			#self.t2listWidget2.addItem(str(self.filenames[len(self.filenames) - 1]))
#系统退出
	def Quit(self,action):#退出
		#sip.setdestroyonexit(QtGui.QApplication(sys.argv).exec_())
		self.close()
#用户登录
	def userLogin(self,action):
		#print self.pyqtdb.open()
		if self.ms is None:
			war1 = Warning(self)
			war1.label_warning.setText(u"     请先连接数据库！")
			war1.detail = u"      请输入数据库实例和数据库名\n   并输入远程登录数据库的用户名和密码"
			war1.exec_()

		elif self.host == "" or self.db == "" or self.user == "" or self.pwd == "":
			war1 = Warning(self)
			war1.label_warning.setText(u"  没有设置数据库信息")
			war1.detail = u"      请输入数据库实例和数据库名\n   并输入远程登录数据库的用户名和密码"
			war1.exec_()
		else:
			self.d1 = ulogin(MainWindow)
			self.d1.exec_()
			self.userName=self.d1.user
			self.userFlag=self.d1.flag
			self.userLimits=self.d1.limits
			self.dlabel_serverinfo_2.setText(u"当前用户：")
			if self.userFlag==True:#用户成功登录
				self.dlabel_serverinfo_2.setText(self.dlabel_serverinfo_2.text()+self.d1.user)
				self.dlabel_serverinfo_2.setStyleSheet(_fromUtf8("color: rgb(0, 85, 255);\n"))
#系统设置
	def Setting(self,action):
		try:
			#print "SETTING"
			setting1 = Setting(self)
			setting1.exec_()
			self.ip = str(setting1.ip)
			self.host = str(setting1.host)
			self.db = str(setting1.db)
			self.user = str(setting1.user)
			self.pwd = str(setting1.pwd)
			#self.ms  = MSSQL(host=self.ip+"\\"+self.host, user=self.user, pwd=self.pwd, db=self.db)
			#self.pyqtdb.setDatabaseName(
				#'DRIVER={SQL SERVER};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s;' % (self.ip+"\\"+self.host, self.db, self.user, self.pwd))
			#self.pyqtdb.open()
			self.dcombox_name.setCurrentIndex(0)
		except:
			pass

#----------------------------------------------------------
	def S1(self):#显示连接上数据库还是文件系统
		self.ms = MSSQL(self.host, user=self.user, pwd=self.pwd, db=self.db)
		self.pyqtdb = QtSql.QSqlDatabase.addDatabase('QODBC')
		self.pyqtdb.setDatabaseName(
			'DRIVER={SQL SERVER};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s;' % (self.host, self.db, self.user, self.pwd))


		#self.pyqtdb.setDatabaseName(
			#'DRIVER={MYSQL};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s;' % (self.ip+"\\"+self.host, self.db, self.user, self.pwd))
		if self.actionS1.isChecked()==True:
			self.pyqtdb.open()
			self.on_dcombox_place_A()
		else:
			self.pyqtdb.close()
			self.ms=None
#---------------------------------------------------------
	def StartDialog(self):#显示StartDialog
		self.sd=StartDialog(self)
		self.sd.exec_()




#---------------------------------------------------------


	#---------------------------------------------------------
	#各个窗口的显示函数
	def Main(self):#中央画图区域
		if self.actionMain.isChecked() == True:
			self.centralWidget.show()
		elif self.actionMain.isChecked() == False:
			self.centralWidget.hide()

	def databaseShow(self):#数据库显示区域
		if self.dockWidget_database.isVisible() == True:
			self.dockWidget_database.hide()
			self.actionV1.setChecked(False)
			self.actionDataBase.setChecked(False)
		else:
			self.dockWidget_database.show()
			self.actionV1.setChecked(True)
			self.actionDataBase.setChecked(True)
		#if self.actionDataBase.isChecked()==True:
		#   self.dockWidget_database.show()
		#elif self.actionDataBase.isChecked()==False:
		#  self.dockWidget_database.hide()

	def CompareShow(self):#对比分析
		if self.dockWidget_compare.isVisible() == True:
			self.dockWidget_compare.hide()
			self.actionV2.setChecked(False)
			self.actionCompare.setChecked(False)
		else:
			self.dockWidget_compare.show()
			self.actionV2.setChecked(True)
			self.actionCompare.setChecked(True)

	def ControlShow(self, p0):#用户控制台
		if self.dockWidget_Control.isVisible() == True:
			self.dockWidget_Control.hide()
			#self.actionV3.setChecked(False)
			self.actionControl.setChecked(False)
		else:
			self.dockWidget_Control.show()
			#self.actionV3.setChecked(True)
			self.actionControl.setChecked(True)

	def DetailShow(self):#详细信息
		if self.dockWidget_Detail.isVisible() == True:
			self.dockWidget_Detail.hide()
			self.actionV4.setChecked(False)
			self.actionDetail.setChecked(False)
		else:
			self.dockWidget_Detail.show()
			self.actionV4.setChecked(True)
			self.actionDetail.setChecked(True)

	def CalendarShow(self):#日期显示
		if self.dockWidget_calender.isVisible() == True:
			self.dockWidget_calender.hide()
			self.actionV5.setChecked(False)
			self.actionCalender.setChecked(False)
		else:
			self.dockWidget_calender.show()
			self.actionV5.setChecked(True)
			self.actionCalender.setChecked(True)
		#---------------------------------------------------------

	def P1(self):#快速绘图
		print self.actionS1.isChecked()

	def P2(self):#2-D柱状图
		print self.actionS1.isChecked()

	def P3(self):#2-D饼状图
		print self.actionS1.isChecked()

	def P4(self):
		print self.actionS1.isChecked()

	def P5(self):
		print self.actionS1.isChecked()

	def P6(self):
		print self.actionS1.isChecked()

	#----------------------------------------------------------


	def T2(self):#远程连接
		print self.actionS1.isChecked()
#--------------------------------------------------------------
#API介绍
	def H1(self):
		print self.actionS1.isChecked()
#--------------------------------------------------------------
#程序介绍 系统相关
	def About(self):
		print self.actionS1.isChecked()
#排序
	def Sort(self,action):
		if action==self.actionAscend:
			temp=self.df[self.df.columns[self.columnChooseIndex[0]+6]].copy()
			temp.sort(axis=0,kind='quicksort',order=None,ascending=True)
			#temp.sort()
			print temp
		print "jiangxu"




#--------------------------------------------------------------
	#DataBase窗口中的一些函数
	@pyqtSignature("bool")
	def on_dcheckBoxX_clicked(self, checked):
		if checked == True:
			self.dcheckBoxY.setChecked(False)
			self.dcheckBoxZ.setChecked(False)
		else:
			self.Xindex = -1
			#self.Xresult=[]
			#self.dlineEdit_X.setText(" ")


	@pyqtSignature("bool")
	def on_dcheckBoxY_clicked(self, checked):
		if checked == True:
			self.dcheckBoxX.setCheckState(0)
			self.dcheckBoxZ.setChecked(False)
		else:
			self.Yindex = -1


	@pyqtSignature("bool")
	def on_dcheckBoxZ_clicked(self, checked):
		if checked == True:
			self.dcheckBoxX.setCheckState(0)
			self.dcheckBoxY.setChecked(False)
		else:
			self.Zindex = -1


	@pyqtSignature("QString")
	def on_dlineEdit_X_textChanged(self, p0):
		if p0 == "":
			self.Xresult = []
			self.dlineEdit_X.setText(" ")


	def on_dlineEdit_Y_textChanged(self, p0):
		if p0 == "":
			self.Yresult = []
			self.dlineEdit_Y.setText(" ")


	@pyqtSignature("QString")
	def on_dlineEdit_Z_textChanged(self, p0):
		if p0 == "":
			self.Zresult = []
			self.dlineEdit_Z.setText(" ")


	def addX(self,a):
		self.Xresult = []
		self.Xindex = a
		if self.isProcess==False:
			self.dlineEdit_X.setText("X : " + str(self.df.columns[self.Xindex + 6]))
			self.Xresult = np.array(self.df[self.df.columns[self.Xindex + 6]])
			if self.df.columns[self.Xindex + 6] == "Date":
				for tab in range(len(self.Xresult)):
					tempdate=QDate.fromString(self.Xresult[tab],"yy-MM-dd")
					tempdate.setYMD(tempdate.year()+100,tempdate.month(),tempdate.day())
					self.Xresult[tab] =tempdate.toPyDate()
			elif self.df.columns[self.Xindex + 6] == "Time":
				for tab in range(len(self.Xresult)):
					self.Xresult[tab] = QTime.fromString(self.Xresult[tab]).toPyTime()
					#self.Xresult[tab]=np.datetime_as_string(self.Xresult[tab])
			else:
				pass
		else:
			self.dlineEdit_X.setText("X : " + str(self.ts1.columns[0]))
			tempx=[]
			for tab in xrange(len(self.ts1[self.ts1.columns[0]])):
				#print self.ts1[self.ts1.columns[0]][0]
				#print type(self.ts1[self.ts1.columns[0]][0])
				(val1,val2)=str(self.ts1[self.ts1.columns[0]][tab]).split(' ',1)
				tempx.append( QTime.fromString(val2).toPyTime())
			self.Xresult = np.array(tempx)
			#print self.Xresult



		#str1="select ID,Year,Month,Day,Hour,Minute,Second "+" from "+self.tablename+self.sqlstr_condition+self.sqlstrtail
		#temp_time=self.ms.ExecQuery(str1)
		#for tab1 in range(len(temp_time)):
		#self.Xresult.append(datetime.datetime(int(temp_time[tab1][1])+2000, int(temp_time[tab1][2]),\
		#int(temp_time[tab1][3]),int(temp_time[tab1][4]),int(temp_time[tab1][5]),int(temp_time[tab1][6])))
		#self.Xresult=np.array()

	def addY(self, a):
		tempstr = self.dlineEdit_Y.text()
		self.Yindex = a
		if self.isProcess==False:
			tempstr = tempstr + 'Y' + str(tempstr.count('Y')) + ':' + str(self.df.columns[self.Yindex + 6]) + ', '
			self.dlineEdit_Y.setText(tempstr)
			#str1="select "+str(self.ms.title[a])+" from "+self.tablename+self.sqlstr_condition+self.sqlstrtail
			self.Yresult.append(np.array(self.df[self.df.columns[self.Yindex + 6]]))
		else:
			tempstr = tempstr + 'Y' + str(tempstr.count('Y')) + ':' + str(self.ts1.columns[self.Yindex]) + ', '
			self.dlineEdit_Y.setText(tempstr)
			#str1="select "+str(self.ms.title[a])+" from "+self.tablename+self.sqlstr_condition+self.sqlstrtail
			self.Yresult.append(np.array(self.ts1[self.ts1.columns[self.Yindex]]))
		self.YcountA=self.YcountA+1
		self.columnChooseIndex.append(a)

	def addZ(self, a):
		self.Zindex = self.columnChooseIndex[0]
	def addXYZ(self,action):
		if action==self.setX:
			self.addX(self.currentChoose)
			self.columnChooseIndex=[]
		elif action==self.setY:
			self.addY(self.currentChoose)



	def dbsectionClicked(self, a):
		self.columnChooseIndex=[]
		self.currentChoose=a
		self.columnChooseIndex.append(a)
		modifier=QtGui.QApplication.keyboardModifiers()
		if modifier==QtCore.Qt.ControlModifier:
			self.setX.setDisabled(True)
			self.setY.setDisabled(True)
			self.setZ.setDisabled(True)
			self.statisMenu.setDisabled(True)

			self.corr.setEnabled(True)
			self.YcountB=self.YcountB+1
			self.Yresult.append(np.array(self.df[self.df.columns[self.currentChoose + 6]]))
		else:
			#self.columnChooseIndex=[]
			self.YcountB=1
			self.setX.setEnabled(True)
			self.setY.setEnabled(True)
			self.setZ.setEnabled(True)
			self.statisMenu.setEnabled(True)

			self.corr.setDisabled(True)
		#self.columnChooseIndex.append(a)





	def dbsectionDoubleClicked(self, a):
		if self.dcheckBoxX.isChecked() == True:
			self.addX()
		elif self.dcheckBoxY.isChecked() == True:
			self.addY(a)
		elif self.dcheckBoxZ.isChecked() == True:
			self.addZ(a)

	def dbRightClicked(self,table):
		rightMenu = QtGui.QMenu(table)
		# 可以指定自定义对象事件


		rightMenu.addMenu(self.PlotMenu)
		self.PlotMenu.addSeparator()

		self.CutAction = QtGui.QAction(u"剪切..(T)   Ctrl+T", self, triggered=self.Cut)
		rightMenu.addAction(self.CutAction)
		self.CopyAction = QtGui.QAction(u"复制..(C)   Ctrl+C", self, triggered=self.Copy)
		rightMenu.addAction(self.CopyAction)
		self.PasteAction = QtGui.QAction(u"粘贴..(V)   Ctrl+V", self, triggered=self.Paste)
		rightMenu.addAction(self.PasteAction)

		rightMenu.addSeparator()

		rightMenu.addAction(self.setX)
		rightMenu.addAction(self.setY)
		rightMenu.addAction(self.setZ)

		rightMenu.addSeparator()
		rightMenu.addAction(self.process)
		rightMenu.addSeparator()
		rightMenu.addAction(self.corr)
		rightMenu.addSeparator()
		rightMenu.addAction(self.fivePJ)
		rightMenu.addSeparator()
		rightMenu.addMenu(self.statisMenu)



		quitAction = QtGui.QAction(u"退出", self, triggered=self.close)
		rightMenu.addAction(quitAction)


		rightMenu.exec_(QtGui.QCursor.pos())

	#--------------------------------------------------------------
	def Stastics(self,action):
		if action==self.count:
			print self.columnChooseIndex
			print self.df[self.df.columns[self.columnChooseIndex[0]+6]].count()
		elif action==self.description:
			#print "\t\t"
			print self.df[self.df.columns[self.columnChooseIndex[0]+6]].describe()
	def fivePinjun(self,action):
		#datetime.datetime.strptime("12:10:20",'%H:%M:%S')
		#date_time = datetime.datetime.strptime("2012-10-20",'%Y-%m-%d')
		#.resample(rule="5M",how="mean")
		#time=pandas.tseries.index.DatetimeIndex
		time=[]
		for tab in xrange(len(self.df["Time"])):

			#print datetime.datetime.strptime(self.df["Date"][tab]+' '+self.df["Time"][tab],'%Y-%m-%d %H:%M:%S')
			time.append(datetime.datetime.strptime(self.df["Date"][tab]+' '+self.df["Time"][tab],'%Y-%m-%d %H:%M:%S'))
		#time=pandas.PeriodIndex(time,freq='S')

		ts=Series(np.array(self.df[self.df.columns[self.columnChooseIndex[0]+6]]), index=time)

		#self.ts1=pandas.DataFrame({"DateTime":ts.index,self.df.columns[self.columnChooseIndex[0]+6]:ts})

		temps1=ts.resample("5Min")
		self.ts1=pandas.DataFrame({"DateTime":temps1.index,self.df.columns[self.columnChooseIndex[0]+6]:temps1})
		self.dataModel = DataFrameModel()
		self.dtableView.setModel(self.dataModel)
		self.dataModel.setDataFrame(self.ts1)
		self.dataModel.signalUpdate()
		self.dtableView.resizeColumnsToContents()
		self.dtableView.show()
		self.isProcess=True


		#print Series(self.df[self.df.columns[self.columnChooseIndex[0]+6]]).resample("5Min")


	#------------------------------------------------------------
	#以下是一些实用的函数，如查询、绘图等
	#-------------------------------------------------------------
	def Cut(self):
		pass
	def Copy(self):
		print self.currentChoose
		self.dataModel2 = DataFrameModel()
		self.tableView.setModel(self.dataModel2)
		names2=[self.df.columns[self.columnChooseIndex[tab]+6] for tab in range(len(self.columnChooseIndex))]
		self.dataModel2.setDataFrame(DataFrame(self.df[names2[0:len(names2)]]))
	def Paste(self):
		self.dataModel2.signalUpdate()
		self.tableView.resizeColumnsToContents()
#数据导入Import
	def Import(self,action):#数据导入
		if self.userFlag==True and self.userLimits==0:
			if self.dcombox_name.currentIndex() > 0:
				import1 = Import(self)
				import1.exec_()
			else:
				war1 = Warning(self)
				war1.label_warning.setText(u"      数据库表连接失败!")
				war1.detail = u"       请检查是否选择了数据表!"
				war1.exec_()
		else:
			war1 = Warning(self)
			war1.label_warning.setText(u"您没有登录或不具有管理员权限")
			war1.detail = u"      请确保您已经成功登录\n   并确保您的账户具有管理员权限！"
			war1.exec_()

#数据删除Delete
	def Delete(self):#数据删除
		if self.userFlag==True and self.userLimits==0:
			try:
				delete1 = Delete(self)
				delete1.exec_()
			except:
				war1 = Warning(self)
				war1.label_warning.setText(u"     请选择数据库表！")
				war1.detail = u"      "
				war1.exec_()
		else:
			war1 = Warning(self)
			war1.label_warning.setText(u"您没有登录或不具有管理员权限")
			war1.detail = u"      请确保您已经成功登录\n   并确保您的账户具有管理员权限！"
			war1.exec_()

#数据下载
	def D5(self):
		print self.actionS1.isChecked()
#数据处理
	def Process(self):
		process=Process(self)
		process.exec_()
		time=[]
		PP=process.combine.split('\\')

		for tab in xrange(len(self.df["Time"])):
			time.append(datetime.datetime.strptime(self.df["Date"][tab]+' '+self.df["Time"][tab],'%Y-%m-%d %H:%M:%S'))
		#time=pandas.PeriodIndex(time,freq='S')

		ts=Series(np.array(self.df[self.df.columns[self.columnChooseIndex[0]+6]]), index=time)

		#self.ts1=pandas.DataFrame({"DateTime":ts.index,self.df.columns[self.columnChooseIndex[0]+6]:ts})

		#temps1=eval("ts."+str(PP[0])+'.'+'("'+str(PP[1])+'")')

		if str(PP[0])=="resample":
                        temps1=ts.resample(str(PP[1]))
		self.ts1=pandas.DataFrame({"DateTime":temps1.index,self.df.columns[self.columnChooseIndex[0]+6]:temps1})
		self.dataModel = DataFrameModel()
		self.dtableView.setModel(self.dataModel)
		self.dataModel.setDataFrame(self.ts1)
		self.dataModel.signalUpdate()
		self.dtableView.resizeColumnsToContents()
		self.dtableView.show()
		self.isProcess=True


#数据绘图
	def Plot(self,action):


		#self.mplwidget.axes.clear()
		flag_index=['b','g','r','c','m','y','k','w','b*','g*','r*','c*','m*','y*','k*','w*']
		if action==self.S:
			print u"描点"
			flag="r*"
		elif action==self.L:
			print u"直线"
			flag="b"
		temp5=[]
		if self.YcountA>self.YcountB:
			temp=self.YcountA
		else:
			temp=self.YcountB
		self.mplwidget.axes.hold(True)
		if self.YcountA>1:
			self.mplwidget.temp1=[]
			if self.isProcess==False:
				for tab in range(temp):
					self.mplwidget.axes.plot(self.Xresult, self.Yresult[tab],flag_index[tab],label=str(self.labelA)+self.df.columns[self.columnChooseIndex[tab]+6])
				self.mplwidget.temp1.append(self.df.columns[self.columnChooseIndex[tab]+6])
			elif self.isProcess==True:
				for tab in range(temp):
					self.mplwidget.axes.plot(self.Xresult, self.Yresult[tab],flag_index[tab],label=str(self.labelA)+self.ts1.columns[self.columnChooseIndex[tab]])
				self.mplwidget.temp1.append(self.ts1.columns[self.columnChooseIndex[tab]])
		else:
			A=len(self.mplwidget.temp1)
			if self.isProcess==False:
				self.mplwidget.axes.plot(self.Xresult, self.Yresult[A],flag_index[A],label=str(self.labelA)+self.df.columns[self.columnChooseIndex[A]+6])
				self.mplwidget.temp1.append(self.df.columns[self.columnChooseIndex[A]+6])
			else:
				self.mplwidget.axes.plot(self.Xresult, self.Yresult[A],flag_index[A],label=str(self.labelA)+self.ts1.columns[self.columnChooseIndex[A]])
				self.mplwidget.temp1.append(self.ts1.columns[self.columnChooseIndex[A]])


		self.mplwidget.MyLegend(tuple(self.mplwidget.temp1))
		self.labelA=self.labelA+1
		self.mplwidget.draw()
		#self.mplwidget.draw()
		#self.mplwidget.axes.clear()
		#self.mplwidget.draw()
	#self.mplwidget.figure.colorbar(self.mplwidget.draw)
		self.YcountA=0
		self.YcountB=0
#数据查询
	def Query(self,action):
		self.Xresult = []
		self.Yresult = []
		self.Zresult = []
		self.mplwidget.temp1=[]
		self.YcountA=0
		self.YcountB=0
		self.dlineEdit_X.setText(" ")
		self.dlineEdit_Y.setText(" ")
		self.dlineEdit_Z.setText(" ")
		self.sqlstrtail = ""
		for tab1 in range(self.dlistWidget.count()):
			tempstr = unicode(self.dlistWidget.item(tab1).text()).encode("utf-8")
			self.sqlstrtail = self.sqlstrtail + " and " + tempstr
		self.idcount = 0
		t1 = time.clock()
		self.dlabel_Col.setText("")
		self.dlabel_Row.setText("")
		self.dlabel_time.setText("")
		try:
			a = unicode(self.dcombox_name.currentText())
			self.tablename = self.tablenamedict[a]
			#if 'SQLSERVER' in self.host:
			if 1>0:
				#datetime1=str(self.ddate1.date().toPyDate())
				datetime1 = self.ddateTimeEdit1.text().split(' ')
				datetime2 = self.ddateTimeEdit2.text().split(' ')
				#date1 = datetime1[0].replace("/","-")
				#date2 = datetime2[0].replace("/","-")
				#date1 = datetime1[0].split('/')
				#date2 = datetime2[0].split('/')
				date1=self.ddateTimeEdit1.date().toPyDate()
				date2=self.ddateTimeEdit2.date().toPyDate()
				time1 = datetime1[len(datetime1) - 1].split(':')
				time2 = datetime2[len(datetime2) - 1].split(':')

				#self.sqlstr_condition = " where (((Year)*32141000+Month*2678400+Day*86400+Hour*3600+Minute*60+Second)/100000) between " + str(
					#float(int(date1[0]) * 32141000 + int(date1[1]) * 2678400 + int(date1[2]) * 86400 + int(
						#time1[0]) * 3600 + int(time1[1]) * 60 + int(time1[2])) / 100000) \
										#+ " and " + str(float(
					#int(date2[0]) * 32141000 + int(date2[1]) * 2678400 + int(date2[2]) * 86400 + int(
						#time2[0]) * 3600 + int(
						#time2[1]) * 60 + int(time2[2])) / 100000)

				#datetime1=str(self.ddateTimeEdit1.time())
				#self.sqlstr_condition = " where Date>\'"+str(date1)+"\' and "+"Date<\'"+str(date2)+"\'"
				self.sqlstr_condition = " where Date>\'"+str(date1)+"\' and "+"Date<\'"+str(date2)+"\'"
				sqlstr = "select * from " + self.tablename + self.sqlstr_condition + self.sqlstrtail + " ORDER BY ID ASC"
				#or "((Year*32141000+Month*2678400+Day*86400+Hour*3600+Minute*60+Second)/100000) between "+str(float(int(date1[0])*32141000+int(date1[1])*2678400+int(date2[2])*86400+int(time1[0])*3600+int(date1[1])*60+int(date2[2]))/100000)\
				#+" and "+str(float(int(date2[0])*32141000+int(date2[1])*2678400+int(date2[2])*86400+int(time2[0])*3600+int(time2[1])*60+int(date2[2]))/100000)+" ORDER BY ID ASC"
				if self.ms.GetConnect() == True:
					if 1 > 0:
						#resList=self.ms.ExecQuery(sqlstr)
						#self.idcount=len(resList)
						if self.ddateTimeEdit1.date().toPyDate() < self.ddateTimeEdit2.date().toPyDate():
							try:
								#显示数据
								#df = psql.frame_query(sqlstr, self.ms.conn)
								self.df = psql.read_frame(sqlstr, self.ms.conn)
								self.idcount = self.df['ID'].count()


								#datetime=[str(int(x)+2000)+'-'+str(int(y))+'-'+str(int(z))+" "+str(int(u))+':'+str(int(v))+':'+str(int(w)) \
								#for x, y, z, u, v, w in zip(tuple(df.Year), tuple(df.Month), tuple(df.Day), tuple(df.Hour), tuple(df.Minute), tuple(df.Second))]
								#self.df["Date1"]=pd.to_datetime(datetime)#在df.columns后再加一列Date1
								#names=[self.df.columns[tab] for tab in range(len(self.df.columns))]
								#names.insert(7,names[len(names)-1])#将增加的一列插入到前列中
								#names.pop(len(names)-1)#去掉最后一列的Date1

								names = [self.df.columns[tab] for tab in range(len(self.df.columns))]
								names.insert(7, names[0])
								self.dataModel = DataFrameModel()

								self.dtableView.setModel(self.dataModel)

								#self.dataModel.setDataFrame(self.df)
								self.dataModel.setDataFrame(self.df[names[7:len(names)]])
								#sys.stdout=saveout
								#pd.rolling_sum(self.df, 60).plot(subplots=True)
								self.dataModel.signalUpdate()
								self.dtableView.resizeColumnsToContents()
								#self.model.setQuery(sqlstr)
								#model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
								#self.dtableView.setModel(self.model)
								#设置表头显示与否
								self.dtableView.verticalHeader().setVisible(False)
								self.dtableView.horizontalHeader().setMovable(True)
								self.dtableView.show()
								self.dlabel_Col.setText(str(self.dtableView.horizontalHeader().count()))
								self.dlabel_Row.setText(str(self.idcount))
								self.dlabel_time.setText(str(time.clock() - t1)[0:4] + 's')
							except Exception as err1:
								pass
						else:
							self.dtableWidget.hide()
							war3 = Warning(self)
							war3.label_warning.setText(u"   数据获取失败!")
							war3.detail = u"   请检查表中是否有有效的记录!"
							war3.exec_()

					else:
						#self.dtableView.hide()
						war3 = Warning(self)
						war3.label_warning.setText(u"     数据获取失败!")
						war3.detail = u"    请检查输入的表是否存在!"
						war3.exec_()
				else:
					war2 = Warning(self)
					war2.label_warning.setText(u"   数据库连接失败!")
					war2.detail = u"请检查输入的数据库及其相关信息是否有效!"
					war2.exec_()
			else:
				war1 = Warning(self)
				war1.label_warning.setText(u"   数据库服务无法找到!")
				war1.detail = u"        请选择正确的数据库实例"
				war1.exec_()
		except:
			pass
		#----------------------------------------------------------

		#----------------------------------------------------------------
 #数据打印
 	def Print(self):
		printer = QtGui.QPrinter(QtGui.QPrinter.HighResolution)
		printDialog = QtGui.QPrintDialog(printer, self)
		if printDialog.exec_() == QtGui.QDialog.Accepted:
			painter = QtGui.QPainter(printer)
			rect = painter.viewport()
			size = self.image.size()
			size.scale(rect.size(), QtCore.Qt.KeepAspectRatio)
			painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
			painter.setWindow(self.image.rect())
			painter.drawImage(0, 0, self.image)
			painter.end()

	@pyqtSignature("QString")
	def on_dcombox_name_currentIndexChanged(self, p0):
		if self.dcombox_name.currentIndex() > 0:
			#print type(unicode(p0).encode("utf-8"))
			self.tablename = self.tablenamedict[unicode(p0)]
			sqlstr = "select * from " + self.tablename
			try:

				if self.ms.GetConnect() == True:
					self.ms.ExecNonQuery(sqlstr)
				#self.dcombox_index.addItems(self.ms.title)
				self.dcombox_index.insertItems(0, self.ms.title)

			except:
				war1 = Warning(self)
				war1.label_warning.setText(u"   数据库表无法找到!")
				war1.detail = u"      请选择正确的数据库"
				war1.exec_()

			#for tab in range(len(self.ms.title)):
			#self.dcombox_index.addItem(self.ms.title[tab])
	def on_dcombox_place_A(self):
			sqlstr = "select * from tb_Place"
			tempresult=[]
			try:
				if self.ms.GetConnect() == True:
					for tab in range(len(self.ms.ExecQuery(sqlstr))):
						tempresult.append(unicode(self.ms.ExecQuery(sqlstr)[tab][2]).encode("utf-8").decode("utf-8"))
				self.dcombox_place.insertItems(0, tempresult)
			except:
				war1 = Warning(self)
				war1.label_warning.setText(u"   地点无法找到!")
				war1.detail = u"      请选择正确的地点"
				war1.exec_()
#dcombox_place
	@pyqtSignature("")
	def on_dpb_add_clicked(self):
		a = unicode(self.dlineEdit1.text()).encode("utf-8")
		b = unicode(self.dlineEdit2.text()).encode("utf-8")
		c = unicode(self.dcombox_con.currentText()).encode("utf-8")
		tempstr = c.replace("...", "  " + str(a) + "  ", 1).replace("...", "  " + str(b))
		print tempstr
		self.dlistWidget.addItem(self.dcombox_index.currentText() + "  " + tempstr.decode("utf-8"))


	@pyqtSignature("")
	def on_dpb_clear_clicked(self):
		self.dlistWidget.clear()


	@pyqtSignature("QListWidgetItem*")
	def on_dlistWidget_itemClicked(self, item):
		self.dlistWidget.tempitem = item


	@pyqtSignature("")
	def on_dpb_delete1_clicked(self):
		self.dlistWidget.takeItem(self.dlistWidget.row(self.dlistWidget.tempitem))
#监听键盘事件
	def keyPressEvent(self,event):
		if event.key()==QtCore.Qt.Key_Escape:
			self.close()




	"""
@pyqtSignature("QModelIndex")
    def on_dtableView_activated(self, index):
        if self.flag2%2==0:
            self.dtableView.setSelectionBehavior(0)
        else:
            self.dtableView.setSelectionBehavior(1)
        self.flag2=self.flag2+1

	"""

	def getWidget(self, splash):
		t = QtCore.QElapsedTimer()
		t.start()
		while (t.elapsed() < 1000):
			str = QtCore.QString("       loading = ") + QtCore.QString.number(t.elapsed())
			splash.showMessage(str)
			QtCore.QCoreApplication.processEvents()

	@pyqtSignature("QModelIndex")
	def on_dtableView_clicked(self, index):
		pass


	@pyqtSignature("QModelIndex")
	def on_dtableView_pressed(self, index):
		pass

	@pyqtSignature("QModelIndex")
	def on_dtableView_doubleClicked(self, index):
		war1=Warning(self)
		war1.label_warning.setText(u"   地点无法找到!")
		war1.detail = u"      请选择正确的地点"
		war1.exec_()
		row=index.row()
		col=index.col()
		value=0
		self.df.set_value(row, col, value)
		print self.df.set_value(row, col, value)
		print "AAA"


if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	splash_pix = QPixmap(u"splash_loading.png")
	splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
	splash.setMask(splash_pix.mask())
	splash.show()
	app.processEvents()

	#pixmap = QtGui.QPixmap(u"splash_loading.png")
	#splash = QtGui.QSplashScreen(pixmap)
	#label = QtGui.QLabel(splash)
	#label.setText("<br>       <br>Foxreal")
	#label.setAlignment(QtCore.Qt.AlignRight)
	#splash.show()
	#QtCore.QCoreApplication.processEvents()
	#time.sleep(2)
	MainWindow = MainWindow()
	#splash.finish(MainWindow.getWidget(splash))

	MainWindow.show()
	splash.finish(MainWindow)
	sip.setdestroyonexit(app.exec_())
    

