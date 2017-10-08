#coding:utf8
'''
状态模式：当一个对象的内在状态改变时允许改变行为，用于控制一个对象状态的条件表达式过于复杂的情况
这里用到了state模块，需要
pip install state
感觉就是状态之间的转换，将大而乱的代码修改为小而简，易于给维护
'''

def workday():
    print 'work hard!'
def weekend():
    print 'play harder!'
class People(object): pass
people = People()

for i in xrange(1, 8, 1):
    if i == 6:
        people.day = weekend
    if i == 1:
        people.day = workday
    people.day()
        
