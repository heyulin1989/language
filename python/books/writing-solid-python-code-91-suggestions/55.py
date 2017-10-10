#coding:utf8
'''
init不是初始化的方法
当需要覆盖__new__(), __init__()方法时，两个参数参数要保持一致
'''
class A(object):
    def __new__(cls, *args, **kargs):
        print cls
        print args
        print kargs
        print '------------------'
        instance = object.__new__(cls, *args, **kargs)
        #print instance
        return instance
    def __init__(self, a, b):
        print "init gets called"
        print "self is", self
        self.a, self.b = a, b
#a1 = A(1,  2, k=3)
a1 = A(1,  2)
print a1.a
print a1.b

'''
何时需要覆盖__new__()方法
'''

# 1.当类继承的不可变型对象且默认的__new__()方法不能满足需要时
# 不可变型对象: str, int, unicode, tuple, frozenset
class UserSet(frozenset):
    '''
    这个方法不能满足需要
    输入:   "I am string
    输出:   "I" "am" "string"
    需要用到 __new__
    '''
    def __init__(self, arg=None):
        if isinstance(arg, basestring):
            arg = arg.split()
        frozenset.__init__(self, arg)

    def __new__(cls, *args):
        if args and isinstance(args[0], basestring):
            args = (args[0].split(), ) + args[1:]
        return super(UserSet, cls).__new__(cls, *args)
        
print UserSet("I am string")
print frozenset("I am testing ")

'''
用来实现工厂模式或者单例或者进行元类编程的时候
'''
class Shape(object):
    def __init__(object):
        pass
    def draw(self):
        pass
class Triangle(Shape):
    def __init__(self):
        print "I am a tringle"
    def draw(self):
        print "I am drawing triangle"

class Rectangle(Shape):
    def __init__(self):
        print "I am a Rectangle"
    def draw(self):
        print "I am drawing triangle"
class Trapezoid(Shape):
    def __init__(self):
        print "I am a Trapezoid"
    def draw(self):
        print "I am drawing triangle"
        
class Diamond(Shape):
    def __init__(self):
        print "I am a diamond"
    def draw(self):
        print "I am drawing triangle"
class ShapeFactory(Shape):
    shapes = {'triangle':Triangle, 'rectangle': Rectangle, 'trapezoid': Trapezoid, 'diamond': Diamond}
    def __new__(klass, name):
        if name in ShapeFactory.shapes.keys():
            print "creating a new shape %s" % name
            return ShapeFactory.shapes[name]()
        else:
            print "creating a new shape %s" % name
            return Shape()

ShapeFactory('rectangle').draw()

'''
作为用来初始化的__init__()方法在多继承的状态下，子类的__init__()方法如果不显式的调用
父类的方法不会被调用
'''
class A(object):
    def __init__(self):
        print "I am A's __init__"
class B(A):
    def __init__(self):
        print "I am B's __init__"

B()
