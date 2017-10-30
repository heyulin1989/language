#coding:utf8
'''
闭包的概念: 一个函数和它的环境变量合在一起，就构成了一个闭包(closure)
'''

def line_conf():
    b = 15
    c = 16
    def line(x):
        c = 2000
        return 2*x + b + c
    return line

my_line = line_conf()
print my_line.__closure__
# 这个闭包中的__closure__包含一个元组，元组中的每一个元素都是cell类型的对象
print my_line.__closure__[0].cell_contents
#print my_line.__closure__[1].cell_contents
print my_line(my_line(5))
'''
python使用self的原因
1.受其他语言的影响
Andrew: What other languages and systems have influnced Python's design?
Guido: There have have many. ABC was a major influnce,  of course, since I have been working on it 
       at CWI. It inspired the use of indentation to delimit blocks, which are the high-level types
       and parts of object implementation. I'd spent a summer at DEC's Systems Research Center,
       where I was introduced to Modula-2+; The Modular-3 final report was being written there at 
       about the same time.What I learned there showed up in Python's exception handling, modules
       and the fact that methods explicitly contain "self" in their parameter list. String slicing 
       come from Algol-68 and Icon.

2.Python语言本身的动态性决定了使用self能够带来一定的便利
3.在存在同名的变量以及实例变量的情况下使用self使得实例变量更容易被区分

Python的哲学:  Explicit is better than implicit
'''
