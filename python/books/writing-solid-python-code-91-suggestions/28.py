#coding:utf8
# 直接格式化字符或者数值
print "your score is %06.1f" % 9.5
# 以元组的形式格式化
import math
itemname = 'circumference'
radius = 3
print "the %s of a circle with radius %f is %0.3f " % (itemname, radius, math.pi*radius*2)
# 以字典的形式格式化
itemdict = {'itemname':'circumference', 'radius':3, 'value':math.pi*radius*2}
print "the %(itemname)s of a circle with radius %(radius)f is %(value)0.3f " % itemdict

#使用位置符号
print "The number {0:,} in hex is: {0:#x}, the number {1} in oct is {1:#o}".format(4746, 45)
#使用名称 
print "The max number is {max}, the min number is {min}, the average number is {average:0.3f}".format(max=189, min=12.6, average=23.5)
#通过属性
class Customer(object):
	def __init__(self, name, gender, phone):
		self.name = name
		self.gender = gender
		self.phone = phone
	def __str__(self):
		return 'Customer({self.name},{self.gender},{self.phone})'.format(self=self)

print str(Customer("Lisa", "Female", "67889"))
# 格式化元组的具体项
point = ((1, 3),(2,4))
print 'X:{0[0]};Y:{0[1]}'.format(point)



"""
建议使用format
"""
