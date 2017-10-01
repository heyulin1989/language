#coding:utf8
def appendtest(newitem, lista = []):
	print id(lista)
	lista.append(newitem)
	print id(lista)
	return lista


#appendtest('a', ['b',2,4,[1,2]])
print appendtest(1)
print appendtest.func_defaults
print appendtest('a')
print appendtest.func_defaults

# 默认的参数所指向的对象在所有的函数调用中被共享
# 如果函数调用需要动态生成则使用None对象作为占位符

# 如下
"""
def appendtest(newitem, lista = None):
	if lista is None:
		lista = []
	lista.append(newitem)
	return lista
"""
