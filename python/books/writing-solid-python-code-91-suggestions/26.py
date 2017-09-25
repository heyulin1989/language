class A:
	i=1
"""
	def __nonzero__(self):
		print 'testing A.__nonzero__()'
		return True
	def __len__(self):
		print "get length"
		return False
"""

if A():
	print 'not empty'
else:
	print "empty"

