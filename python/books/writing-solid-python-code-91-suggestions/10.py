from time import time
t = time()
abbrevitions = ['cf.','e.g.','ex.','etc.','fig.','i.e.','Mr.','vs.']
for i in xrange(100000):
	for w in ('Mr.', 'Hat', 'is', 'chasing', 'the', 'black', 'cat', '.'):
		#if w in abbrevitions:
		if w[-1] == '.' and  w in abbrevitions:
			pass

print "total run time:"
t1 = time()
print t1-t

for i in xrange(100000):
	for w in ('Mr.', 'Hat', 'is', 'chasing', 'the', 'black', 'cat', '.'):
		if w in abbrevitions:
		#if w[-1] == '.' and  w in abbrevitions:
			pass
print "total run time"
print time() - t1
