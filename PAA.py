#coding:utf-8

def paa(path_file, x, y, W_Size=5):
    import os
    from decimal import *
    import time
    getcontext().prec=3
    t1=time.clock()
    path=os.getcwd()
    output="PAA_OUTPUT"
    if not os.path.isdir(path+"\\"+output):
        os.makedirs(path+"\\"+output)
    if not os.path.isdir(path+"\\"+"NIHEWUCHA_OUTPUT"):
        os.makedirs(path+"\\"+"NIHEWUCHA_OUTPUT")
    temp=0
    A=[]
    B=[]
    #加上第一个端点
    A.append(Decimal(x[0])*1)
    B.append(Decimal(y[0])*1)
    for tab in range(0,len(y),W_Size):
        for tab2 in range(W_Size):
            if tab+tab2<=len(y)-1:
                temp=temp+float(y[tab+tab2])
            else:
                #print "**********"+str(temp)
                tab2=tab2-1
                break
        if tab+tab2<len(y)-1:
            A.append(Decimal(x[tab+tab2/2])*1)
        else:
            A.append(Decimal(x[len(y)-1])*1)#加上最后一个端点
        B.append(str(Decimal(temp/(tab2+1))+0))
        temp=0
    
    D=[]
    for tab in range(0,len(B)-1):
        a1=float(B[tab])
        b1=float(B[tab+1])
        for tab2 in range(W_Size):
            D.append(str(Decimal(a1+(b1-a1)*tab2/W_Size)+0))
    #添加序列减去N个窗口后的剩余序列
    a2=b1
    b2=float(y[len(y)-1])
    tab2=0
    while len(D)<len(y):
        D.append(str(Decimal(a2+(b2-a2)*tab2/(len(y)-(tab+1)*W_Size))+0))
    

    temp=path_file.split("\\")
    filename=temp[len(temp)-1]
    with open(path+"\\"+'NIHEWUCHA_OUTPUT'+'\\'+"PAA___NIHEWUCHA"+filename,"w")as f_out1,\
    open(path+'\\'+output+'\\'+'PAA'+filename,"w")as f_out2:
        #写入拟合误差操作序列
        for tab in range(len(y)):
            f_out1.write(str(Decimal(x[tab])*1)+'\t')
            f_out1.write(str(Decimal(y[tab])*1)+'\t')
            f_out1.write(str(D[tab])+'\n')
        for tab in range(len(B)):
            f_out2.write(str(A[tab])+'\t')
            f_out2.write(str(B[tab])+'\n')
        #把分段后的序列写到文件中
        for tab in range(len(x)):
            x.pop(0)
        for tab in range(len(A)):
            x.append(A[tab])
        for tab in range(len(y)):
            y.pop(0)
        for tab in range(len(B)):
            y.append(B[tab])

    #print "Time eclipse:"+str(time.clock()-t1)
    #print u"PAA压缩比为"+str(Decimal(float(W_Size-1)/W_Size)+0)
                
                
