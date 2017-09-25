#coding:utf8
import timeit
strlist=["it is a long value string will not keep in memory" for n in range(100000)]
#print strlist
# 尽量使用join来连接字符串 

def join_test():
	return ''.join(strlist)

def plus_test():
	result=''
	for i,v in enumerate(strlist):
		result = result + v
	return result

if __name__ == '__main__':
	jointimer = timeit.Timer("join_test()","from __main__ import join_test")
	print jointimer.timeit(number = 100)
	jointimer = timeit.Timer("plus_test()","from __main__ import plus_test")
	print jointimer.timeit(number = 100)

