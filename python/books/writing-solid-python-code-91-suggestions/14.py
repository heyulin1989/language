#encoding:utf8
import sys
from math import *
"""
尽量不使用eval
"""
def ExpCalcBot(string):
	try:
		print 'Your answer is', eval(string)
	except NameError:
		print "The expression you enter is not valid"
print 'Hi, I am ExpCalcBot, please input your expression or enter e to end'
inputstr=''
while 1:
	print 'Please enter a number or operation. Enter c to complete. :'
	inputstr= raw_input()
	if inputstr == str('e') :
		sys.exit()
	elif repr(inputstr) != repr(''):
		ExpCalcBot(inputstr)
		inputstr = ''
