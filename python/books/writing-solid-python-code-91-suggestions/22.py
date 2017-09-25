#with open("test.py", 'w') as f:
#	f.write("test")

class MyContextManager(object):
	def __enter__(self):
		print "entering....."
	def __exit__(self, exception_type, exception_value, traceback):
		print "leaving....."
		if exception_type is None:
			print "no exceptions!"
			return False
		elif exception_type is ValueError:
			print "value error!!!"
			return True
		else:
			print "other error"
			return True

with MyContextManager():
	print "Testing..."
	raise(ValueError)
