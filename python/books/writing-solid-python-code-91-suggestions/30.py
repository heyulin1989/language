#coding:utf8

nested_list = [['Hello', "world"], ['Goodbye', 'World']]
# [expr for iter_item in iterable if cond_expr]
nested_list = [[s.upper() for s in xs if len(s) > 5] for xs in nested_list ]
print nested_list

# 支持多重迭代
nested_list = [(a,b) for a in ['a','1'] for b in [3,'b'] if a != b]
print (nested_list)

# 表达式可以是函数
def f(v):
	if v%2 == 0:
		v = v**2
	else:
		v = v+1
	return v

nested_list = [f(v) for v in [2,3,4,5,6,7,-1] if v>0]
print nested_list
#也可以是普通的计算
nested_list = [v**2 if v%2==0 else v+1 for v in [2,3,4,5,6,7,-1,-2] if v>0]
print nested_list

# 可以把iterable当作一个文件句柄
fh = open("23.py","r")
result = [i for i in fh if 'print' in i]
print result
# 元组，集合，字典都可以
# 字典  ===>> {expr1, expr2 for iter_item in iterable if cond_expr}
# 集合  ===>> {expr for iter_item in iterable if cond_expr}
# 元组  ===>> (expr for iter_item in iterable if cond_expr)


