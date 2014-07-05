#coding:utf-8
def plrefp(path_file, x, y, K=5):
    import os
    import math
    import time
    #import datetime
    #start=datetime.datetime.now().microsecond
    from decimal import *
    getcontext().prec=3
    t1= time.clock()
    path=os.getcwd()
    output="PLR_EFP"
    if not os.path.isdir(path+'\\'+output):
        os.makedirs(path+'\\'+output)
    if not os.path.isdir(path+"\\"+"NIHEWUCHA_OUTPUT"):
        os.makedirs(path+"\\"+"NIHEWUCHA_OUTPUT")
    
    yasuo_length=0
    zong_length=0
    
    L=[]#新建下标列表
    val_1=float(y[1])-float(y[0])
    for tab in range(len(y)-1):
        val_2=float(y[tab+1])-float(y[tab])
        if val_1==0 and val_2==0:
            continue
        #添加极值点和一部分拐点 
        if (val_1>0 and val_2<=0) or (val_1>=0 and val_2<0)or(\
        val_1<0 and val_2>=0) or (val_1<=0 and val_2>0):
            L.append(tab)
        #添加另一部分拐点
        elif 0<abs(val_2/val_1)<1/float(K) or K<abs(val_2/val_1):
            L.append(tab)
        val_1=val_2
    #插入两个端点
    L.insert(0,0)
    L.insert(len(L),len(y)-1)
    #对特征点的下标序列L进行筛选
    tab=0
    while tab<len(L)-2:
        if L[tab+1]-L[tab]<=K and L[tab+1]-L[tab+2]<=K:
            L.remove(L[tab+1])
            tab=tab-1
        tab=tab+1
    yasuo_length=yasuo_length+len(L)
    zong_length=zong_length+len(y)
    #计算直线插补的序列D
    D=[]
    for tab in range(len(L)-1):
        for tab1 in range(0,L[tab+1]-L[tab]):
            a=float(y[L[tab]])
            b=float(y[L[tab+1]])
            D.append(str(Decimal(a+(b-a)*tab1/(L[tab+1]-L[tab]))+0))
    D.append(str(Decimal(b)+0))
    
    temp=path_file.split("\\")
    filename=temp[len(temp)-1]
    with open(path+"\\"+'NIHEWUCHA_OUTPUT'+'\\'+"PLR_EFP___NIHEWUCHA"+filename,"w")as f_out1,\
    open(path+"\\"+output+"\\"+'PLR_EFP'+filename,"w")as f_out2:
        #写入拟合误差操作序列
        for tab in range(len(y)):
            f_out1.write(str(x[tab])+'\t')
            f_out1.write(str(y[tab])+'\t')
            f_out1.write(D[tab]+'\n')
        #把分段后的序列写到文件中
        for tab in range(len(L)):
            f_out2.write('%8s'%(str(x[L[tab]])+'  '))
            f_out2.write('%8s'%(str(y[L[tab]])+'  '))
            f_out2.write("\n")
     
    A=x[0:len(x)]
    B=y[0:len(y)]    
    for tab in range(len(x)):
        x.pop(0)
        y.pop(0)
    for tab in range(len(L)):
        x.append(A[L[tab]])
        y.append(B[L[tab]])
        
    #end=datetime.datetime.now().microsecond
    #plr_ee_time=end-start
    #print end
    #print datetime.datetime.now()
    #print plr_ee_time
    #print time.clock()
    #print "Time eclipse:"+str(time.clock()-t1)
    #print u"PLR_EFP压缩比："+str(float(zong_length-yasuo_length)/zong_length)
    return float(zong_length-yasuo_length)/zong_length


