# -*- coding: utf-8 -*-
#import pymssql
import pyodbc
from Warning import *
#cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.1.100\\sql;DATABASE=ImageDB;UID=sa;PWD=111')
#cursor = cnxn.cursor()
#cursor.execute("select * from Tb")
#coding=utf-8 
#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name: pymssqlTest.py
# Author: scott
#
# Created: 04/02/2012
#-------------------------------------------------------------------------------

class MSSQL:
    def __init__(self,host,user,pwd,db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def GetConnect(self):
        if not self.db:
            raise(NameError,"没有设置数据库信息")

        #self.conn = pyodbc.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset="utf8")
        self.connection_info='DRIVER={SQL Server};SERVER='+self.host+';DATABASE='+self.db+';UID='+self.user+';PWD='+self.pwd
        try:
            self.conn=pyodbc.connect(self.connection_info)
            return True
        except:
            return False

    def ExecQuery(self,sql):
        try:
            self.cur = self.conn.cursor()
            self.cur.execute(sql)
            resList = self.cur.fetchall()
            return resList
        except:
            return False 
    def ExecNonQuery(self,sql):
        try:
            self.cur = self.conn.cursor()
            #self.cur.execute(sql)
            self.title=[]
            self.maxID=len(self.cur.execute(sql).fetchall())
            index=self.cur.description
            #print "AAAAAA"
            #print self.maxID
            #print "BBBBBB"
            for i in range(len(index)):
                self.title.append(str(index[i][0]))
        except:
            pass
           # self.cur = self.GetConnect()
            #self.cur = self.conn.cursor()
            #self.cur.executemany(sql)
            #self.conn.commit()
            #self.conn.close()

    def ExecuteImport(self,sql):
        try:
            self.GetConnect()
            self.cur = self.conn.cursor()
            self.cur.execute(sql)
            self.conn.commit()
            self.conn.close()
            #self.cur = self.__GetConnect()
            return "success"
        except:
            return "Failed"
    def ExecuteDelete(self,sql):
        try:
            self.GetConnect()
            self.cur = self.conn.cursor()
            self.cur.execute(sql)
            self.conn.commit()
            self.conn.close()
            #self.cur = self.__GetConnect()
            return "success"
        except:
            return "Failed"
    def GetHeader(self,sql):
        try:
            self.GetConnect()
            self.cur = self.conn.cursor()
            self.cur.execute(sql)
            index=self.cur.description
            self.title=[]
            for i in range(len(index)):
                self.title.append(str(index[i][0]).encode("utf-8"))
            self.conn.close()
            return self.title
        except:
            pass    
    def Closed(self):
        try:
            #self.cur.conn.commit()
            self.conn.close()
            return "Closed Success"
        except:
            return "Closed Failed"
#def main(tablename):
    #ms = MSSQL(host="PC-20130605JMCY\MSSQLSERVERCM",user="sa",pwd="111",db="imageDB")
    #resList = ms.ExecQuery("select * from "+tablename)
    #resList = ms.ExecQuery("select name from SysObjects where type='U' ")
    #print resList
    #for tab in resList:
        #print str(tab[1]).decode("utf8").strip()
        #print str(tab)
    #print ms.title

#if __name__ == '__main__':
    #main("tb_Airda16000_1")

