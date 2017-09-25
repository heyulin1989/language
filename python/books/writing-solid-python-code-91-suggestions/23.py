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
			if i % j == 0:
				break
		else:
			print '%d is a prime number' % i

print print_prime2(20)
