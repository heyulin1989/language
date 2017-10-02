#coding:utf8
import ConfigParser
conf = ConfigParser.ConfigParser()
conf.read('example.conf')
#print conf.get('section1', 'in_default')

#  支持字典输出
print '%(protocol)s://%(server)s:%(port)s/' % {'protocol':'http', 'server':'example.com', 'port':1080}

print conf.get('db1', 'conn_str')
print conf.get('db2', 'conn_str')
