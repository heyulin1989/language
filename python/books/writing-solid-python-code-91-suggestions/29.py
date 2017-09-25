#coding:utf8

"""
 数字，字符串和元组为不可变.
 字典，列表，字节数组为可变
"""
class Student(object):
	"""
	def __init__ (self, name, course=[]):
		self.name = name
		self.course = course
	"""
	def __init__ (self, name, course=None):
		self.name = name
		if course is None:course = []
		self.course = course

	def addcourse(self, coursename):
		self.course.append(coursename)
	def printcourse(self):
		for item in self.course:
			print item


stuA = Student("Wang yi")
stuA.addcourse("English")
stuA.addcourse("Math")
print stuA.name+"'s course:"
stuA.printcourse()
print "-------------"
stuB = Student("Li san")
stuB.addcourse("Chinese")
stuB.addcourse("Physics")
print stuB.name+"'s course:"
stuA.printcourse()


# 在实例化对象时，两个对象分配了不同的内存空间
# 并且调用init()函数初始化，但是由于init()函数的第二个参数为默认参数，默认参数在被调用时仅仅被评估一次
# 解决方案：传入None，在创建的时候动态生成列表
print "stuA.course = {0:#x}, stuB.course={1:#x}".format(id(stuA.course), id(stuB.course))
# 切片操作为浅copy

# python 是一切皆是对象，Java基本类型不是对象
a=1
print id(a)	
print id(1)
a+=2
print id(a)	
str1 = "hello-world"
str2 = str1
str1 = str1[:-5]
print str1
print str2
