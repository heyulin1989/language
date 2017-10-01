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


str="123 123 123 123"
# replace不指定就全部替换
print str.replace("123", "321")
# 指定需要替换的个数
print str.replace("123", "321", 2)

# 对于切片知识的学习
str="123456789"
print str[1:2]  # 输出 2   [1,2)   str 从0开始
print str[0:2]  # 输出 12  
print str[-2:-1] # 输出 8  [-2, -1)  
print str[0:-1] #  输出 12345678  [0, -1)
print str[:-2]  # 输出 1234567
"""
     "123456789"
位置  012345678
                       ... -3 -2 -1
"""


# split陷阱
str=' hello    world!'
# 先去除字符串的两端空白，然后以任意长度的空白字符串为分隔符
print str.split()   # ====>  ['hello', 'world!']
print str.split(' ')  # ==>  ['', 'hello', '', '', '', 'world!']
print ''.split()   # ===> []
print ''.split(' ')  # ===> ['']

# title : 将每个单词的首写字母大写
print str.title()
# string.capwords : 将两端的空白字符串去除,然后将中间多余的空白字符串去除
import string
print string.capwords(str)
# expandtabs([tabsize]) : 将tab转换为适当数量的空格, 默认为8
