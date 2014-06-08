# -*- coding: utf-8 -*-
"""import numpy as np
from PyQt4.QtCore import Qt
from PyQt4.QtGui import *
from matplotlib.backends.backend_qt4 import NavigationToolbar2QT as NavigationToolbar
from plot_dialog2 import Ui_Form

class PlotDialog(QWidget, Ui_Form):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.navi_toolbar = NavigationToolbar(self.plot_canvas, self)
        self.plot_layout.addWidget(self.navi_toolbar)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    dialog = PlotDialog()
    dialog.show()
    sys.exit(app.exec_())
"""
"""import pyodbc
import pandas.io.sql as psql
from pandas import *
import numpy as np
connection_info="DRIVER={SQL Server};SERVER=127.0.0.1\MSSQLSERVERCM;DATABASE=ImageDB;UID=sa;PWD=111"
cnxn = pyodbc.connect(connection_info) 
cursor = cnxn.cursor()
sql = "SELECT * FROM JDMCL"

df = psql.frame_query(sql, cnxn)
#newdf = df[df.columns[2:4]]
"""
"""def get_id_by_name(name):
    return len(name)
def validate(myid,myage):
    if myid<myage:
        return True
    else:
        return False
def check_data(info):
    name, age, height = info
    id = get_id_by_name(name)
    return validate(id, age)

print check_data(['xiaoming',12,170])"""

"""
#df["Date"]=to_datetime(['14-01-2012', '01-14-2012'],dayfirst=True)
#datetime=[]
#print str(int(df.Year[0])+2000)+"-"+str(int(df.Month[0]))+"-"+str(int(df.Day[0]))+" "+\
#      str(int(df.Hour[0]))+":"+str(int(df.Minute[0]))+":"+str(int(df.Second[0]))
datetime=[str(int(df.Year[tab])+2000)+"-"+str(int(df.Month[tab]))+"-"+str(int(df.Day[tab]))+\
                " "+str(int(df.Hour[tab]))+":"+str(int(df.Minute[tab]))+":"+str(int(df.Second[tab])) for tab in range(len(df.Year))]
#for tab in range(len(df.Year)):
#    datetime.append(str(int(df.Year[tab])+2000)+"-"+str(int(df.Month[tab]))+"-"+str(int(df.Day[tab]))+\
#                " "+str(int(df.Hour[tab]))+":"+str(int(df.Minute[tab]))+":"+str(int(df.Second[tab])))

print len(datetime)
df["Date"]=to_datetime(datetime)

names=[df.columns[tab] for tab in range(len(df.columns))]
#for tab in range(len(df.columns)):
#    names.append(df.columns[tab])
names.insert(7,names[len(names)-1])
names.pop(len(names)-1)

print names
print df[names[7:len(names)-1]].describe()
#cnxn.close()
"""
"""# -*- coding:gbk -*-
'''示例2: 替换函数(装饰)
装饰函数的参数是被装饰的函数对象，返回原函数对象
装饰的实质语句: myfunc = deco(myfunc)'''
 
def deco(func):
    print("before myfunc() called.")
    func()
    print("  after myfunc() called.")
    return func
 
def myfunc():
    print(" myfunc() called.")
 
myfunc1 = deco(myfunc)
 
#myfunc1()
#myfunc1()
"""
"""
# -*- coding:gbk -*-
'''示例3: 使用语法糖@来装饰函数，相当于“myfunc = deco(myfunc)”
但发现新函数只在第一次被调用，且原函数多调用了一次'''
 
def deco(func):
    print("before myfunc() called.")
    func()
    print("  after myfunc() called.")
    return func
 
@deco
def myfunc():
    print(" myfunc() called.")
 
myfunc()
myfunc()

print "AAA"
"""
"""# -*- coding:gbk -*-
'''示例4: 使用内嵌包装函数来确保每次新函数都被调用，
内嵌包装函数的形参和返回值与原函数相同，装饰函数返回内嵌包装函数对象'''
 
def deco(func):
    def __deco1():
        print("before myfunc() called.")
        func()
        print("  after myfunc() called.")
        # 不需要返回func，实际上应返回原函数的返回值
    return __deco1
 
#@deco

def myfunc():
    print(" myfunc() called.")
    return 'ok'
myfunc = deco(myfunc) 
print myfunc()
print myfunc()
"""
"""def deco_functionNeedDoc(func):
    if func.__doc__ == None :
        print func, "has no __doc__, it's a bad habit."
    else:
        print func, ':', func.__doc__, '.'
    return func
@deco_functionNeedDoc
def f():
    print 'f() Do something'
@deco_functionNeedDoc
def g():
    'I have a __doc__'
    print 'g() Do something'
f()
g()
"""
"""
import sys 

import urllib
import urllib2
from BeautifulSoup import BeautifulSoup
question_word =u"吃货 程序员"


#temp=question_word.decode("utf-8").encode("utf-8")
#print urllib.quote(temp)
#print sys.getdefaultencoding() 
#print sys.stdin.encoding
#print question_word.encode("utf-8")
url = "http://www.baidu.com/s?wd=" + urllib.quote(question_word.encode("gbk"))
print url

#url=http://www.baidu.com/#wd=%E5%90%83%E8%B4%A7%20%E7%A8%8B%E5%BA%8F%E5%91%98&rsv_spt=1&issp=1&rsv_bp=0\
#&ie=utf-8&tn=baiduhome_pg&rsv_sug3=18&rsv_sug4=856&rsv_sug1=1&rsv_sug2=0&inputT=6372
htmlpage = urllib2.urlopen(url).read()
soup = BeautifulSoup(htmlpage)
#print sys.stdin.encoding
#print soup.title
print len(soup.findAll("a"))
for result_table in soup.findAll("a"):
    a_click = result_table.find("a")
    print "-----标题----\n" + a_click.renderContents()#标题
    print "----链接----\n" + str(a_click.get("href"))#链接
    print "----描述----\n" + result_table.find("div", {"class": "c-abstract"}).renderContents()#描述
    print
"""
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Function:
【教程】Python中第三方的用于解析HTML的库：BeautifulSoup

http://www.crifan.com/python_third_party_lib_html_parser_beautifulsoup

Author:     Crifan Li
Version:    2012-12-26
Contact:    admin at crifan dot com
"""

"""from BeautifulSoup import BeautifulSoup
"""
def beautifulsoupDemo():
    demoHtml = """
<html>
<body>
<div class="icon_col">
        <h1 class="h1user">crifan</h1>
 </div>
 </body>
</html>
""";
"""    soup = BeautifulSoup(demoHtml);
    print "type(soup)=",type(soup); #type(soup)= <type 'instance'>
    print "soup=",soup

    # 1. extract content
    # method 1: no designate para name
    #h1userSoup = soup.find("h1", {"class":"h1user"});
    # method 2: use para name
    h1userSoup = soup.find(name="h1", attrs={"class":"h1user"});
    # more can found at:
    #http://www.crummy.com/software/BeautifulSoup/bs3/documentation.zh.html#find%28name,%20attrs,%20recursive,%20text,%20**kwargs%29
    print "h1userSoup=",h1userSoup; #h1userSoup= <h1 class="h1user">crifan</h1>
    h1userUnicodeStr = h1userSoup.string;
    print "h1userUnicodeStr=",h1userUnicodeStr; #h1userUnicodeStr= crifan

if __name__ == "__main__":
    beautifulsoupDemo();
    """
"""
# coding=utf8
import urllib2
import string
import urllib
import re
import random

#设置多个user_agents，防止百度限制IP
user_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0', \
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0', \
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533+ \
        (KHTML, like Gecko) Element Browser 5.0', \
        'IBM WebExplorer /v0.94', 'Galaxy/1.0 [en] (Mac OS X 10.5.6; U; en)', \
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)', \
        'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14', \
        'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) \
        Version/6.0 Mobile/10A5355d Safari/8536.25', \
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/28.0.1468.0 Safari/537.36', \
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; TheWorld)']

def baidu_search(keyword,pn):
    p= {'wd': keyword}
    res=urllib2.urlopen(("http://www.baidu.com/s?"+urllib.urlencode(p)+"&pn={0}&cl=3&rn=100").format(pn))
    html=res.read()
    return html
def getList(regex,text):
    arr = []
    res = re.findall(regex, text)
    if res:
        for r in res:
            arr.append(r)
    return arr
def getMatch(regex,text):
    res = re.findall(regex, text)
    if res:
        return res[0]
    return ""
def clearTag(text):
    p = re.compile(u'<[^>]+>')
    retval = p.sub("",text)
    return retval

def geturl(keyword):
    for page in range(10):
        pn=page*100+1
        html = baidu_search(keyword,pn)

        content = unicode(html, 'utf-8','ignore')
        arrList = getList(u"<table.*?class=\"result\".*?>.*?<\/a>", content)
        for item in arrList:
            regex = u"<h3.*?class=\"t\".*?><a.*?href=\"(.*?)\".*?>(.*?)<\/a>"
            link = getMatch(regex,item)
            url = link[0]
            #获取标题
            #title = clearTag(link[1]).encode('utf8')

            try:
                domain=urllib2.Request(url)
                r=random.randint(0,11)
                domain.add_header('User-agent', user_agents[r])
                domain.add_header('connection','keep-alive')
                response=urllib2.urlopen(domain)
                uri=response.geturl()
                print uri
            except:
                continue

if __name__=='__main__':
    geturl('python')
"""


# -*- coding:utf8 -*-
# 2013.12.36 19:41 wnlo-c209
# 抓取dbmei.com的图片。

from bs4 import BeautifulSoup
import os, sys, urllib2

# 创建文件夹，昨天刚学会
path = os.getcwd()   				     # 获取此脚本所在目录
new_path = os.path.join(path,u'豆瓣妹子')
if not os.path.isdir(new_path):
	os.mkdir(new_path)


def page_loop(page=0):
	url = 'http://www.dbmeizi.com/?p=%s' % page
	content = urllib2.urlopen(url)

	soup = BeautifulSoup(content)

	my_girl = soup.find_all('img')

    # 加入结束检测，写的不好....
	if my_girl ==[]:
		print u'已经全部抓取完毕'
		sys.exit(0)

	print u'开始抓取'
	for girl in my_girl:
		link = girl.get('src')
		#flink = 'http://www.dbmeizi.com/' + link
		flink =link
		print flink
		content2 = urllib2.urlopen(flink).read()
		with open(u'豆瓣妹子'+'/'+flink[-11:],'wb') as code:#在OSC上现学的
			code.write(content2)
	page = int(page) + 1
	print u'开始抓取下一页'
	print 'the %s page' % page
	page_loop(page)

page_loop()
