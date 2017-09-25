#coding:utf8

nested_list = [['Hello', "world"], ['Goodbye', 'World']]
# [expr for iter_item in iterable if cond_expr]
nested_list = [[s.upper() for s in xs if len(s) > 5] for xs in nested_list ]
print nested_list

# 支持多重迭代

