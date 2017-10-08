#coding:utf8
'''
这个需要了解一下message库
message: 内部类似下面的sub()和pub()方法，还支持取消订阅(unsub())
python-message的消息订阅是全局的，可能存在名字冲突，需要
'''

import Broker_52 as broker

def greeting(name):
    print 'hello, %s.'%name
broker.sub('greet', greeting)
broker.pub('greet', 'LaoLi')
