#coding:utf8

'''
使用ElementTree解析XML
xml.dom.minidom和xml.sax在python2.0以来成为标准库

dom: 需要将整个XML文件加载到内存中并解析成一棵树，占用内存多，性能不占优势
sax: 基于事件驱动，处理过程复杂

ElementTree  >= python2.5
cElementTree是ElementTree的Cython实现，速度更快

ElementTree:  使用简单，内存消耗明显低于dom，支持XPath查询

如果XML文件近似G级别，lxml会获得较优效果
'''
import xml.etree.ElementTree as ET
tree = ET.ElementTree(file="43_test.xml")
root = tree.getroot()
print root
print root.tag
for i in root.findall("system/purpose"):
    print i.text

