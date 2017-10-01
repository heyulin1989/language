#coding:utf8
# python的函数传参既不是引用也不是值
n=3
print "n={:#x}".format(id(n))
def inc(n):
	print "n={:#x}".format(id(n))
	n = n+1
	print "n={:#x}".format(id(n))

inc(n)
print "n={:#x}".format(id(n))


def change_list(orginator_list):
	print "orginator list is: {}".format(orginator_list)
	new_list = orginator_list
	new_list.append("I am new")	
	print "new list is:{}".format(new_list)
	return new_list

orginator_list = ['a','b','c']
new_list = change_list(orginator_list)
print "orginator_list = {}".format(orginator_list)
print "new_list = {}".format(new_list)
	
# 可变对象传引用,不可变对象传值,也不太准确 
def change_me(org_list):
	print id(org_list)
	new_list = org_list
	print "new_list={:#x}".format(id(new_list))
	if len(new_list) > 5:
		new_list = ['a', 'b', 'c']
	for i, e in enumerate(new_list):
		if isinstance(e,list):
			new_list[i] = "***"
	print new_list
	print "new_list={:#x}".format(id(new_list))

test1= [1, ['a', 1, 3], [2,1],6]
change_me(test1)

