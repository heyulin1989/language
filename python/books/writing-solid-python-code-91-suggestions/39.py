#coding:utf8
# Counter: 计数   {}  是一个字典类型
# 依赖模块: collections
# 支持集合操作 + - & |
# from collection import Counter

some_data=['a','2',2,4,5,'2','b',4,7,'a',5,'d','a','z']

#dict 方法
count_frq = dict()
for item in some_data:
    if item in count_frq:
        count_frq[item] += 1
    else:
        count_frq[item] = 1


print "dict method : ", count_frq

# 使用defaultdict
from collections import defaultdict
count_frq=defaultdict(int)
for item in some_data:
    count_frq[item] += 1
print "defaultdict method :  ",count_frq

# 使用set,list
count_set=set(some_data)
count_list=[]
for item in count_set:
    count_list.append((item, some_data.count(item)))

print "set and list method : ", count_list

# 使用 Counter 
from collections import Counter
print " Counter method : ", Counter(some_data)

print Counter("success")

# 使用 elements()方法来获取key值
print list(Counter(some_data).elements())

# 使用most_common()找到前N个出现频率最高的元素以及它们对应的个数
print Counter(some_data).most_common(3)

# 字典访问不存在的key时会出现错误,Counter返回 0
print (Counter(some_data)['y'])

# update()方法计数器对象相加
c = Counter("success")
print c
c.update("successfully")
print c
# subtract()方法计数器对象相减
c.subtract("successfully")
print c

