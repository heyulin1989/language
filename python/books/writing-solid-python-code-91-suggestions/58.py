#coding:utf8
'''
理解MRO和多继承

Python多继承语法:
  class DerivedClassName(Base1, Base2, Base3)

'''
class A(object):
    def getvalue(self):
        print "return value of A"
    def show(self):
        print "I can show the information of A"
class B(A):
    def getvalue(self):
        print "return value of B"
class C(A):
    def getvalue(self):
        print "return value of C"
    def show(self):
        print "I can show the information of C"
class D(B, C):pass


D().getvalue()
D().show()
print D().mro()
'''
古典类:
return value of B
I can show the information of A

新式类:
return value of B
I can show the information of C

原因:
MRO: Method Resolution Order (方法解析顺序)
MRO不同
古典采用自左至右的深度优先算法
D().getvalue()  :   D => B 
D().show():   D => B => A

新式类采用C3 MRO算法:
这个算法符合广度优先算法

D().getvalue()  :   D => B 
D().show():   D => B => C

尽量避免使用菱形继承
'''
