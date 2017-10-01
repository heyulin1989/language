#coding:utf8
# *args用于接受一个包装为元组形式的参数列表来传递非关键字参数
def SumFun(*args):
	result=0
	for x in args[0:]:
		result += x
	return result

print SumFun(2,4)
print SumFun(2,3,4)
print SumFun()
# 使用**kwargs接受字典形式的关键字参数列表,其中字典的键值对分别表示不可变参数的参数名和值
def category_table(**kwargs):
	for name, value in kwargs.items():
		print '{0} is a kind of {1}'.format(name, value)

category_table(apple='fruit', carrot='vegetable', Python='programming language')
category_table(BMW='Car')


# 使用场景
# 1. 为函数添加一个装饰器
def mydecorator(fun):
	def new(*args, **kwargs):
		return fun(*args, **kwargs)
	return new

# 2. 参数数目不确定,可以考虑使用变长参数.如配置文件
"""
[Defaults]
name = test
version = 1.0
platform = windows
"""

from ConfigParser import ConfigParser
conf = ConfigParser()
conf.read('test.cfg')
conf_dict = dict(conf.items('Defaults'))
def func(**kwargs):
	kwargs.update(conf_dict)
	global name
	name = kwargs.get('name')
	global version
	version = kwargs.get('version')
	global platform
	platform = kwargs.get('platform')
func()
print name, version, platform

# 用来实现函数的多态或者在继承情况下子类需要调用父类的某些方法的时候
class A(object):
	def somefun(self,p1,p2):
		pass
class B(A):
	def myfun(self, p3, *args, **kwargs):
		super(B, self).somefun(*args, **kwargs)

