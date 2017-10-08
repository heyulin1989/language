#coding:utf8
from collections import defaultdict
route_table = defaultdict(list)

def sub(topic, callback):
    if callback in route_table[topic]:
        return
    route_table[topic].append(callback)
def pub(topic, *a, **kw):
    for func in route_table[topic]:
        func(*a, **kw)
