#coding:utf8
"""
# vim: set fileencoding=utf8

from __future__ import unnicode_literals
"""
a="Hi"
b="Hi"
print a is b
print a == b
print "a = ",id(a),"  b = ",id(b)

# 一但有空格就会不在一个内存中
a1 = "I am"
b1 = "I am"
print a1 is b1
print a1 == b1
print "a1 = ",id(a1),"  b = ",id(b1)

"""
is 表示的是对象标示符(object identity): 两个对象是否在同一个内存空间
==  equal 两个对象的值是否相等
"""
