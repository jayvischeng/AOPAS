# -*- coding: utf-8 -*-
#
# Copyright 漏 2009 Pierre Raybaut
# Licensed under the terms of the MIT License

"""
MatplotlibWidget
================

Example of matplotlib widget for PyQt4

Copyright 漏 2009 Pierre Raybaut
This software is licensed under the terms of the MIT License

Derived from 'embedding_in_pyqt4.py':
Copyright 漏 2005 Florent Rougon, 2006 Darren Dale
"""

__version__ = "1.0.0"

from PyQt4.QtGui import QSizePolicy
from PyQt4.QtCore import QSize
#from mpl_toolkits.basemap import Basemap
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as Canvas
from matplotlib.figure import *
from PyQt4 import QtGui
#from mpl_toolkits.basemap import *
from matplotlib import rcParams
import matplotlib.dates as dt
rcParams['font.size'] = 9
import functools
import matplotlib
class MatplotlibWidget(Canvas):
	"""
	MatplotlibWidget inherits PyQt4.QtGui.QWidget
	and matplotlib.backend_bases.FigureCanvasBase

	Options: option_name (default_value)
	-------
	parent (None): parent widget
	title (''): figure title
	xlabel (''): X-axis label
	ylabel (''): Y-axis label
	xlim (None): X-axis limits ([min, max])
	ylim (None): Y-axis limits ([min, max])
	xscale ('linear'): X-axis scale
	yscale ('linear'): Y-axis scale
	width (4): width in inches
	height (3): height in inches
	dpi (100): resolution in dpi
	hold (False): if False, figure will be cleared each time plot is called

	Widget attributes:
	-----------------
	figure: instance of matplotlib.figure.Figure
	axes: figure axes

	Example:
	-------
	self.widget = MatplotlibWidget(self, yscale='log', hold=True)
	from numpy import linspace
	x = linspace(-10, 10)
	self.widget.axes.plot(x, x**2)
	self.wdiget.axes.plot(x, x**3)
	"""
	#-----------------------------------------------------------------------------------

	def __init__(self, parent=None, title='', xlabel='', ylabel='',
				 xlim=None, ylim=None, xscale='linear', yscale='linear',
				 width=4, height=3, dpi=100, hold=False):
		self.figure = Figure(figsize=(width, height), dpi=dpi, facecolor="0.86", tight_layout=True)
		self.axes = self.figure.add_subplot(111)
		#self.axes.set_navigate(True)
		#x=[1, 2, 3]
		#y=[1, 2, 3]
		#print self.axes.hexbin(x, y)
		self.axes.set_title(title)
		self.axes.set_xlabel(xlabel)
		self.axes.set_ylabel(ylabel)
		if xscale is not None:
			self.axes.set_xscale(xscale)
		if yscale is not None:
			self.axes.set_yscale(yscale)
		if xlim is not None:
			self.axes.set_xlim(*xlim)
		if ylim is not None:
			self.axes.set_ylim(*ylim)
		self.axes.hold(hold)

		Canvas.__init__(self, self.figure)
		self.setParent(parent)
		Canvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
		Canvas.updateGeometry(self)
		#ch=self.figure.colorbar(matplotlib.image.Image)


		self.rightMenu=QtGui.QMenu(self)
		# 可以指定自定义对象事件
		self.ReAction = QtGui.QAction(u"刷新", self)
		self.ReAction.triggered.connect(functools.partial(self.Setting,self.ReAction))
		self.addAction(self.ReAction)

		self.BGAction = QtGui.QAction(u"背景设置虚线", self)
		self.BGAction.triggered.connect(functools.partial(self.Setting,self.BGAction))
		self.addAction(self.BGAction)
		self.BGAction.setCheckable(True)

		self.actionConvertX = QtGui.QAction(u"X轴坐标时间转换", self)
		self.actionConvertX.triggered.connect(functools.partial(self.Setting,self.actionConvertX))
		self.addAction(self.actionConvertX)
		#self.actionConvertX.setCheckable(True)
		self.addAction(self.rightMenu.insertSeparator(self.BGAction))

		AddLabel = QtGui.QMenu(u"添加标签", self)

		self.actionLabel1 = QtGui.QAction(u"标签居右上", self)
		self.actionLabel1.triggered.connect(functools.partial(self.Setting,self.actionLabel1))
		self.actionLabel2 = QtGui.QAction(u"标签居左上", self)
		self.actionLabel2.triggered.connect(functools.partial(self.Setting,self.actionLabel2))
		self.actionLabel3 = QtGui.QAction(u"标签居右下", self)
		self.actionLabel3.triggered.connect(functools.partial(self.Setting,self.actionLabel3))
		self.actionLabel4 = QtGui.QAction(u"标签居左下", self)
		self.actionLabel4.triggered.connect(functools.partial(self.Setting,self.actionLabel4))
		self.actionLabel5 = QtGui.QAction(u"自动适应", self)
		self.actionLabel5.triggered.connect(functools.partial(self.Setting,self.actionLabel5))
		AddLabel.addAction(self.actionLabel1)
		AddLabel.addAction(self.actionLabel2)
		AddLabel.addAction(self.actionLabel3)
		AddLabel.addAction(self.actionLabel4)
		AddLabel.addAction(self.actionLabel5)

		self.addAction(self.rightMenu.addMenu(AddLabel))
		#self.actionAddFormula.setCheckable(True)
		#self.addAction(self.rightMenu.insertSeparator(self.actionAddLabel))
		AddLabel.addSeparator()

		self.actionMClear = QtGui.QAction(u"清除画布", self, triggered=self.MClear)
		self.addAction(self.actionMClear)
		#self.actionMClear.setCheckable(True)
		#self.addAction(self.rightMenu.insertSeparator(self.actionAddFormula))

		#self.addAction(self.rightMenu.menuAction())
		#self.addAction(self.MUGroup.menuAction())

		#self.actionMClear.triggered.connect(self.MClear)

		#self.rightMenu.exec_(QtGui.QCursor.pos())

	def Setting(self,action):
		#dt.date2num()
		if action==self.ReAction:
			try:
				print len(self.axes.get_lines())
				#print len(self.axes.get_lines())
				#print self.axes.get_lines()[0]
				for tab in range(len(self.axes.get_lines())):
					#print self.LG.get_lines()[tab]
					#print type(self.LG.get_lines()[tab])
					#print self.axes.get_lines()[tab].get_color()

					self.LG.get_lines()[tab].set_color(self.axes.get_lines()[tab].get_color())
					print "sssss"
					h,l=self.axes.get_legend_handles_labels()

					#print "AAA"
					print l
					#print "BBB"
					#print type(self.LG.get_children())
					#self.LG.set_title(l[tab])
					#print self.LG.get_children()[2]

					self.LG.get_lines()[tab].set_marker(self.axes.get_lines()[tab].get_marker())
					#self.LG=self.MyLegend(l)
					self.MyLegend(tuple(l))
			except:
				pass
			self.draw()
		elif action==self.BGAction:
			#self.figure.grid(self.BGAction.isChecked())
			self.axes.grid(self.BGAction.isChecked())
			self.draw()
		elif action==self.actionConvertX:
			templist1=self.axes.get_xticks()
			templist2=[]
			for tab in range(len(templist1)):
				#templist2.append(str(dt.num2date(int(templist1[tab]))))
				hour=int(templist1[tab])/3600
				min=(int(templist1[tab])-hour*3600)/60
				sec=int(templist1[tab])-hour*3600-min*60
				templist2.append("{0}:{1}:{2}".format(str(hour).zfill(2),str(min).zfill(2),str(sec).zfill(2)))
			print templist2
			self.axes.set_xticklabels(templist2)
			#self.axes.xaxis_date()
			#self.axes.redraw_in_frame()
			#self.axes.xaxis_date()
			self.draw()
			#self.figure.update()
		elif action==self.actionLabel1:
			pass
			#self.LG=matplotlib.legend.DraggableLegend(self.LG,False,"center")
			#self.LG.
			#self.axes.legend(("AAAA","BBBB"))

			#self.draw()
		elif action==self.actionLabel2:
			print "2"
		elif action==self.actionLabel3:
			print "3"
		elif action==self.actionLabel4:
			print "4"
		elif action==self.actionLabel5:
			print "5"
	def MClear(self):
		try:
			self.temp=[]
			self.axes.clear()
			self.BGAction.setChecked(False)
			self.draw()
		except:
			pass
	def sizeHint(self):
		w, h = self.get_width_height()
		return QSize(w, h)


	def minimumSizeHint(self):
		return QSize(10, 10)
	def MyLegend(self,a):
		self.LG=self.axes.legend(a)
		#print a
		self.LG.draggable(state=True)
		#return self.LG

"""
#--------------------------------------------------------------------------------------
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=50, tight_layout=True)
        Canvas.__init__(self, fig)
        self.setParent(parent)
        Canvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        Canvas.updateGeometry(self)
        
        self.axes = fig.add_subplot(111)

        map = Basemap(ax=self.axes)
        map.drawcoastlines()
        map.drawcountries()
        map.drawmapboundary()
        map.fillcontinents(color='coral', lake_color='aqua')
        map.drawmapboundary(fill_color='aqua')

        #self.setWindowTitle("PyQt4 and Basemap -- dbzhang800")
        
#        Canvas.__init__(self, self.fig)
#        self.setParent(parent)
"""


#--------------------------------------------------------------------------------------
"""
#===============================================================================
#   Example
#===============================================================================
if __name__ == '__main__':
    import sys
    from PyQt4.QtGui import QMainWindow, QApplication
    from numpy import linspace
    
    class ApplicationWindow(QMainWindow):
        def __init__(self):
            QMainWindow.__init__(self)
            self.mplwidget = MatplotlibWidget(self, title='Example',
                                              xlabel='Linear scale',
                                              ylabel='Log scale',
                                              hold=True, yscale='log')
            self.mplwidget.setFocus()
            self.setCentralWidget(self.mplwidget)
            self.plot(self.mplwidget.axes)
            
        def plot(self, axes):
            #x = linspace(0, 5)
            #axes.plot(x, x**2)
            #axes.fill(x, x)
            #axes.plot(x, x**3)
            m = Basemap(llcrnrlon=-119, llcrnrlat=22, urcrnrlon=-64,\
urcrnrlat=49, projection='lcc', lat_1=33, lat_2=45,\
lon_0=-95, resolution='h', area_thresh=10000)
            m.bluemarble()
            m.drawcoastlines()
            # draw country boundaries
            m.drawcountries(linewidth=2)
            # draw states boundaries (America only)
            m.drawstates()
            # fill the background (the oceans)
            m.drawmapboundary(fill_color='aqua')
            # fill the continental area
            # we color the lakes like the oceans
            m.fillcontinents(color='coral',lake_color='aqua')
            # draw parallels and meridians
            m.drawparallels(np.arange(25,65,20),labels=[1,0,0,0])
            m.drawmeridians(np.arange(-120,-40,20),labels=[0,0,0,1])
        
    app = QApplication(sys.argv)
    win = ApplicationWindow()
    win.show()
    sys.exit(app.exec_())
"""




