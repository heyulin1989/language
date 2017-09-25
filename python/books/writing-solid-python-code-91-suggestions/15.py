#encoding:utf8
li = ['a','b','c','d']
"""
python2.3k中引入，具有一定的隋性
"""
for i, e in enumerate(li):
	print "index:",i,"element:",e

def myenumerate(sequence, start=0):
	n = -1
	# reversed :用于反转
	for elem in reversed(sequence):
		yield len(sequence)+n, elem
		n -= 1
for i, e in myenumerate(li):
	print "index:",i,"element:",e
