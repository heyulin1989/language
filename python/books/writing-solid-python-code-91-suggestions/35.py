#coding:utf8
class A(object):
	def instance_method(self, x):
		print "calling instance method instance_method(%s, %s)"%(self, x)

	@classmethod
	def class_method(cls, x):
		print "calling class_method(%s,%s)"%(cls, x)
	
	@staticmethod
	def static_method(x):
		print "calling static_method(%s)"%x

a = A()
a.instance_method("test")
a.class_method("test")
a.static_method("test")

class Fruit(object):
	def __init__(self, area="", category="", batch=""):
		self.area = area
		self.category = category
		self.batch = batch
	@staticmethod
	def Init_Product(product_info):
		area, category, batch = map(int, product_info.split('-'))
		fruit = Fruit(area, category, batch)
		return fruit
	@classmethod
	def init_product(cls, product_info):
		area, category, batch = map(int, product_info.split('-'))
		fruit = Fruit(area, category, batch)
		return fruit
		
	total = 0
	@classmethod
	def print_total(cls):
		print cls.total
		print id(Fruit.total)
		print id(cls.total)
	@classmethod
	def set(cls, value):
		print "calling class_method(%s, %s)"%(cls, value)
		cls.total = value
class Apple(Fruit):
	pass
class Orange(Fruit):
	pass

app1 = Apple()
app1.set(200)
#所有的classmethod共享同一个classmethod
app2 = Apple()
app2.set(999)
org1 = Orange()
org1.set(300)
org2 = Orange()
app1.print_total()
org1.print_total()

print '=============================================================================='
app1 = Apple(2,5,10)
org1 = Orange.Init_Product("3-3-9")

print "app1 is instance of Apple: " + str(isinstance(app1, Apple))
print "org1 is instance of Apple: " + str(isinstance(org1, Orange))

