# -*- coding: utf-8 -*-

"""
Module implementing Import.
"""

from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature
from FileOperation import *
from Ui_Import import Ui_Import
from Warning import *
class Import(QDialog, Ui_Import):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        try:
            self.comboBox.insertItems(0, parent.ms.title)
        except:
            war1=Warning(self)
            war1.label_warning.setText(u"   数据库表连接失败!")
            war1.detail=u"请检查是否选择了数据表!"
            war1.exec_()
            Import.done(0)

    
    @pyqtSignature("")
    def on_toolButton_clicked(self):
        #self.dlabel_Col.setText("")                                
        #self.dlabel_Row.setText("")
        #self.dlabel_time.setText("")
        #t1=time.clock()
        #self.idcount=0
        myF=FilesOpera()
        files=myF.FilesImport()

        if files:
            self.dprogressBar.setRange(0, len(files))
            for tab1 in range(len(files)):
                print type(files[tab1][-5])
                f=open(unicode(files[tab1]).encode("utf-8").decode("utf-8"))
                self.dprogressBar.setValue(tab1+1)
                str_file=f.readlines()
                sqlstr1="Select * from JDMCL where ID=1"
                fields=self.ms.GetHeader(sqlstr1)
                for tab2 in range(len(str_file)):
                    str_line=re.split(r"\t *|,| *", str_file[tab2].strip())

                    if '-' in str_line[0]:
                        (year, month, day)=str_line[0].split('-')
                    if ':' in str_line[1]:
                        (hour, minute, second)=str_line[1].split(':')
                    datas=[]
                    #self.idcount=self.idcount+1
                    datas.append(str(self.idcount))
                    datas.append(year)
                    datas.append(month)
                    datas.append(day)
                    datas.append(hour)
                    datas.append(minute)
                    datas.append(second)
                    for tab in range(len(str_line)-2):
                        datas.append(str_line[tab+2])
                    datas.append(u"德令哈")
                    datas.append(unicode(files[tab1][-5]).encode("utf-8")+"m")   
                    sqlstr2="insert into JDMCL"
                    sqlfields=','.join(fields)
                    sqldatas='\',\''.join(datas)
                    sqlstr2=sqlstr2+'('+sqlfields+')'+' values (\''+sqldatas+'\')'
                    #self.ms.ExecuteImport(sqlstr2)
                    #self.model.setQuery(sqlstr2)
                    
            #self.dlabel_time.setText(str(time.clock()-t1)+'  s')
            #print self.tablename
            #print self.ms .GetConnect()
    
    @pyqtSignature("")
    def on_toolButtonFolder_clicked(self):
        myF=FilesOpera()
        folder=myF.FolderImport()
        self.lineEditFolder.setText(folder)
    
    @pyqtSignature("")
    def on_toolButtonFiles_clicked(self):
        myF=FilesOpera()
        files=myF.FilesImport()
        for tab in range(len(files)):
            fullpath=files[tab]
            self.filenames=fullpath.split("\\")
            self.lineEditFiles.insert (str(self.filenames[len(self.filenames)-1])+'  ') 
        self.FileNameFormat.insert(str(self.filenames[len(self.filenames)-1]))
