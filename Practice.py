# -*- coding: utf-8 -*-
__author__ = 'Administrator'
C = {} # 类别计数字典
DA = {} # 特征A的取值计数字典
CDA = {} # 类别和特征A的不同组合的取值计数字典
D=[("Sunny","15","Yes"),("Sunny","10","No"),("Windy","10","No")]
T=-1
A=0
for t in D:
	print  C.get(t[T], 0)
	C[t[T]] = C.get(t[T], 0) + 1
	DA[t[A]] = DA.get(t[A], 0) + 1
	CDA[(t[T], t[A])] = CDA.get((t[T], t[A]), 0) + 1
#PC = map(lambda x: float(x) / len(D), C.values()) # 类别的概率列表
PC = map(lambda x: float(x) / len(D), [1,2])
print PC
#entropy_D = entropy(tuple(PC)) # map返回的对象类型为map，需要强制类型转换为元组

PCDA = {} # 特征A的每个取值给定的条件下各个类别的概率（条件概率）
for key, value in CDA.items():
	a = key[1] # 特征A
	pca = value / DA[a]
	PCDA.setdefault(a, []).append(pca)
#print PC

#print "--------------------------------"

#print PCDA

#print "--------------------------------"

#print CDA