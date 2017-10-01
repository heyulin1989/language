#coding:utf8
a = "hi"
print isinstance(a, str)
b = u"Hi"
print isinstance(b,str)
print isinstance(b,basestring)
print isinstance(b,unicode)
print isinstance(a,unicode)
"""
basestring 是str和unicode的基类
"""

print 'Hello World!'.istitle()
print 'WOrld Hello!'.istitle()

"""
使用in or not in 来判断是否包含子串
"""
str="contains some special"
if "some" in str:
    print "yes"
