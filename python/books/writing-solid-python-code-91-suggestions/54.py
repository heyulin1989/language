#coding:utf8
'''
python中一切皆对象:
内建类型(built-in type)也是对象
字符，列表，内建类型，用户定义的类型，object，type
python2.2之后，引入了新式类(new-style classes)
在新式类中object是所有内建类型的基类,用户所定义的类可以继承自object也可以继承自内建类型
'''
'''
内建类型，object,type,用户自定义的类之间的关系
'''

class A:    # 古典类
    pass
class B(object):
    pass
class C(type):
    pass
class D(dict):   # 继承自内建类型dict
    pass 

a = A()
b = B()
#c = C()
d = D()
print '=======类型========='
print type(object)
print type(type)
print type(a)
print type(b)
#print type(c)
print type(d)
print '=======基类========='
print object.__bases__
print type.__bases__
#print a.__bases__
#print b.__bases__
#print c.__bases__
#print d.__bases__

print '=======基类========='

class TestNewClass:
    __metaclass__ = type
# 这个为type类型，由于 __metaclass__的修改
print type(TestNewClass)
print TestNewClass.__bases__

'''
Object类的比于古典类多定义了一些特殊的方法：
__new__(), __init__(),__delattr__(),__getattribute__(),__setattr__(),__hash__(),__repr__(),__str()__
'''
