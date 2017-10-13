#coding:utf8


class MyClass(object):
    class_attr = 1


# 类属性
print MyClass.__dict__  # 输出类属性表

# 实例属性
my_instance = MyClass()
print my_instance.__dict__  # 输出实例属性表

#先在实例属性中找，找不到再去类属性中查找
print my_instance.class_attr

# 在类方法中添加一个对象的属性，则在实例中可以查到 
MyClass.class_attr2 = 100
print my_instance.class_attr2

# python中内置类型和用户自定义类型是分开的
my_instance.inst_atr='china'
print my_instance.__dict__['inst_atr']
#print MyClass.__dict__['inst_atr']

class MyClass(object):
    def my_method(self):
        print 'my_method'
print MyClass.__dict__['my_method']        
print MyClass.my_method
# 上面这两个类型不同
print  type(MyClass.__dict__['my_method'])
print type(MyClass.my_method)

t = MyClass.my_method.__get__(None, MyClass)
print t
print type(t)

print my_instance.__getattribute__()
