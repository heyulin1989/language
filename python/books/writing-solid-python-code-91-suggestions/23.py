def print_prime(n):
	for i in xrange(2, n):
		found = True
		for j in xrange(2, i):
			if i % j == 0:
				found = False
				break
		if found:
			print '%d is a prime number' % i

def print_prime2(n):
	for i in xrange(2, n):
		for j in xrange(2, i):
			print "i = {}, j = {}".format(i,j)
			if i % j == 0:
				break
		else:
			print '%d is a prime number' % i



print print_prime2(10)
"""
# while else 和for else  当有break时，这个else就会被执行
i = 0
while (i < 10):
	i += 1
	if i == 0:
		break
else:
	print "ok"
"""
