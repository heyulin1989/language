#coding:utf8

'''
json库的支持
simplejson, cjson, yajl, ujson.
ujson, cjson使用C来实现，速度较快
yajl是Cpython版本的JSON实现

dump/dumps : 序列化
load/loads : 反序列化

处理中文需要通过encoding参数指定对应的字符编码

json与python的数据结构存在差异

当大数据量时，建议使用cPickle。
'''

import datetime
from time import mktime
try: import simplejson as json
except ImportError: import json

# json不可对直接序列化datetime
# json.dumps(datetime.datetime.now())

class DateTimeEncoder(json.JSONEncoder):   # 对JSONEncoder进行扩展
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return  obj.strftime('%Y-%m-%d')
        return json.JSONEncoder.default(self, obj)


d = datetime.datetime.now()
print json.dumps(d, cls=DateTimeEncoder)    # 使用cls指定编码器的名称



