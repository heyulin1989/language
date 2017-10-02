#coding:utf8

"""
命令行参数处理库有(标准库)
getopt, optparser, argparse


getopt:
类似于UNIX中的c函数库getopt()
可以处理长短配置项和参数如
-a -b -cfoo -d bar a1 a2
处理结果为两个列表：
一个是(配置项和值):  [('a', ''),('b', ''), ('c','foo'), ('d', 'bar')]
另一个(参数值):  ['a1', 'a2']
存在的问题: 长短配置项需要分开处理, 对于非法参数和必填参数需要手动处理

optparser:
采用声明式的风格，还可以自动生成应用程序的帮助信息.
add_option()功能强大，支持丰富的命令行接口

argparse:
继承了optparser,同时又增加了更多的功能
书写的代码量更少，bug更少
add_argument_group(): 支持参数分组，使的输出信息更加清晰
add_mutually_exclusive_group(required=False): 确保有一个参数或只有一个参数
支持子命令

docopt:
更加先进易用
现在还不在标准库中
http://docopt.org/
"""

# from optparse import OptionParser
# parser = OptionParser()
# parser.add_option("-f", "--file", dest="filename",
#                   help="write report to FILE", metavar="FILE")
# parser.add_option("-q", "--quiet",
#                   action="store_false", dest="verbose", default=True,
#                   help="don't print status messages to stdout")
# (option, args) = parser.parse_args()
# print "option = ",option
# print "args = ",args


import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-o', '--output')
parser.add_argument('-v', dest='verbose', action='store_true')
parser.add_argument('bar', type=argparse.FileType('w'))
parser.add_argument('door', type=int, choices=range(1,4))

# 添加分组
parser = argparse.ArgumentParser(prog='PROG', add_help=False)
group1 = parser.add_argument_group('group1', 'group1 description')
group1.add_argument('foo', help='foo help')
group2 = parser.add_argument_group('group2', 'group2 description')
group2.add_argument('--bar', help='bar help')

args=parser.print_help()
#print args

#import docopt
