#coding:utf8

# sort() and sorted()

persons = [{'name': 'Jon', 'age': 32},
           {'name':'Alan', 'age': 50},
           {'name':'Bob', 'age':32}]
print sorted(persons, key=lambda x:(x['name'], -x['age']))
#[{'age': 50, 'name': 'Alan'}, {'age': 32, 'name': 'Bob'}, {'age': 32, 'name': 'Jon'}]
print (lambda x:(x['name'], -x['age']))(persons[0])
# lambda 表达式
"""
[(lambda x:x*x)(x) for x in range(1,11) if x > 3]  ===> [16, 25, 36, 49, 64, 81, 100]
"""

"""
无论是sort还是sorted 传入cmp参数,速度都比传入key慢
sorted()返回排序后的列表,不改变原数据    >> python2.4
sort()改变原数据,不需要复制原列表,消耗内存少,效率高,返回None.
"""
a=['1',1,'a',3,7,'n']
print a.sort()   #   输出 None
print a   # 输出 [1, 3, 7, '1', 'a', 'n']

# 传入key和cmp参数时，运行的时间比较  约快50%
#from timeit import Timer
#print Timer(stmt="sorted(xs,key=lambda x:x[1])", setup="xs=range(100);xs=zip(xs,xs);").timeit(10000)  # 时间(s) : 0.155812978745
#print Timer(stmt="sorted(xs,cmp=lambda a,b:cmp(a[1],b[1]))", setup="xs=range(100);xs=zip(xs,xs);").timeit(10000)  # 时间(s) : 0.222483873367

# sorted()函数功能强大
# 1. 对字典进行排序
phonebook={'Linda': '7750', 'Bob': '9345', 'Carol': '5834'}
from operator import itemgetter
# phonebook中的号码按照数字大小进行排序
sorted_pb = sorted(phonebook.iteritems(), key=itemgetter(1))
# 输出 :   [('Carol', '5834'), ('Linda', '7750'), ('Bob', '9345')]
print sorted_pb
"""
operator模块中的itemgetter()函数
    def itemgetter(*items):
    if len(items) == 1:
        item = items[0]
        def g(obj):
            return obj[item]
    else:
        def g(obj):
            return tuple(obj[item] for item in items)
    return g

"""
gameresult=[['Bob', 95.00, 'A'], ['Alan', 86.0, 'C'], ['Mandy', 82.5, 'A'], ['Rob', 86, 'E']]
print sorted(gameresult, key=itemgetter(2,1))  # 输出 [['Mandy', 82.5, 'A'], ['Bob', 95.0, 'A'], ['Alan', 86.0, 'C'], ['Rob', 86, 'E']]

print "================================================================================="
# 这个返回的是一个函数,只后再调用函数
# itemgetter() : 这个函数返回的是一个函数
def itemget(*items):
    if len(items) == 1:
        item = items[0]
        def g(obj):
            return obj[item]
    else:
        def g(obj):
            return tuple(obj[item] for item in items)
    return g


print itemget(1)('ABCDEFG')

print "================================================================================="
# 字典中混合list排序
mydict = {
    'Li' : ['M', 7],
    'Zhang' : ['E', 2],
    'Wang'  : ['P', 3],
    'Du'  : ['C', 2],
    'Ma'  : ['C', 9],
    'zhe'  : ['C', 7]
}

print sorted(mydict.iteritems(), key=lambda (k,v):itemgetter(1)(v))
"""
输出: 
[('Zhang', ['E', 2]),
 ('Du', ['C', 2]), 
('Wang', ['P', 3]),
 ('Li', ['M', 7]), 
('zhe', ['C', 7]), 
('Ma', ['C', 9])]
"""


#list 中混合字典

gameresult=[{"name":"Bob", "wins":10, "losses":3, "rating":75.00 },
            {"name":"David", "wins":3, "losses":5, "rating":57.00 },
            {"name":"Carol", "wins":4, "losses":5, "rating":57.00 },
            {"name":"Patty", "wins":9, "losses":3, "rating":71.48 }]
print sorted(gameresult, key=itemgetter("rating", "name"))
"""
 输出:  
[{'wins': 4, 'losses': 5, 'name': 'Carol', 'rating': 57.0},
{'wins': 3, 'losses': 5, 'name': 'David', 'rating': 57.0},
{'wins': 9, 'losses': 3, 'name': 'Patty', 'rating': 71.48},
{'wins': 10, 'losses': 3, 'name': 'Bob', 'rating': 75.0}]
"""
