#encoding:utf-8
"""  数值交换 """
x,y=1,2
print "x = ",x,"  y = ",y
print "after swap"
x,y=y,x
print "x = ",x,"  y = ",y
import dis

def swap1():
	x = 2
	y = 3
	x, y = y, x

def swap2():
	x = 2
	y = 3
	tmp = x
	x = y
	y = tmp

print 'swap1(): '
swap1()
dis.dis(swap1)

print 'swap2(): '
swap2()
dis.dis(swap2)
