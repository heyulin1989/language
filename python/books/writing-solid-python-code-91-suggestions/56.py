#coding:utf8
'''
理解名字的查找机制
'''
a = 1
b = a
c = 'china'

print "local ====>",locals()
print "global ===>", globals()
def foo(x):
    e = 1
    f = e
    g = 'china'
    print '#' * 10
    print "foo(local) ====>",locals()
    print '#' * 10
    print "foo(global) ===>", globals()
    print '#' * 10
    print c

foo(1)
'''
python自2.2之后分为: 
局部作用域(local)
全局作用域(Global)
嵌套作用域(enclosing functions locals)
内置作用域(Build-in)

全局作用域仅在单个文件中

cpython中只要是出现赋值语句时,这个名字就被当作局部变量来处理，
如果要改变为全局变量需要使用global关键字
'''
var = 'c'
def ex2():
    var = 'a'
    def inner():
        global var
        var = 'b'
        print 'inside inner, var is ', var
    inner()
    print 'inside outer function, var is ', var

ex2()    
print 'global var is ', var


'''
下面这段代码出现的 UnboundLocalError错误， 原因是b直接使用没有被定义的局部变量a
使用global解决这个问题会变的复杂, python3中引入了unlocal关键字解决这个问题
def foo1():
    a = 1
    def bar():
        b = a * 2
        a = b + 1
        print 'a  = ', a
    return bar()
foo1()

变量会出现上面的情况，但是dict,list不会出现上面的情况
'''

def outside():
    d = {'outside': 1}
    arr = [1, 2, 3]
    def inside():
        d['inside'] = 2
        arr.append(4)
        print d
        print 'arr = ', arr
    inside()
    print d
    print 'arr = ', arr

outside()
