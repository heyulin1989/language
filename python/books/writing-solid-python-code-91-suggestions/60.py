#coding:utf8

class A(object):
    def __init__(self, name):
        self.name = name
        self.x = 20
    def __getattr__(self, name):
        print ("calling __getattr__:", name)
        if name == 'z':
            return self.x ** 2
        if name == 'y':
            return self.x ** 3
    def __getattribute__(self, attr):
        try:
            return super(A, self).__getattribute__(attr)
        except KeyError:
            return 'default'

a = A("attribute")
print a.name
print a.z
if hasattr(a, 't'):
    c = a.t
    print c
else:
    print "instance a has no attribute t"

class B(object):
    _c = 'test'
    def __init__(self):
        self.x = None
    @property
    def a(self):
        print 'using property to access attribute'
        if self.x is None:
            print 'return value'
            return 'a'
        else:
            print 'error occured'
            raise AttributeError

    @a.setter
    def a(self, value):
        self.x = value
    def __getattr__(self, name):
        print 'using __getattr__ to access attribute'
        print ('attribute name: ', name)
        return "b"
    def __getattribute__(self, name):
        print 'using __getattribute__ to access attribute'
        return object.__getattribute__(self, name)        


a1 = B()    

print a1.a
print "--------------------------"
a1.a = 1
print a1.a
print "--------------------------"
print B._c


        

