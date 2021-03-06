def add(a,b):
	return a+b	
print add(1,2j)
print add('a', 'b')
print add(1, 2)
print add(1.0, 2.3)
print add([1, 2], [3,4])
#print add(1, 'a')

import types
class UserInt(int):
	def __init__(self, val=0):
		self._val = int(val)	
	def __add__(self, val):
		if isinstance(val, UserInt):
			return UserInt(self._val + val._val)
	def __iadd__(self, val):
		raise NotImplementedError("not support operation")
	def __str__(self):
		return str(self._val)
	def __repr__(self):
		return 'Integer(%s)' %self._val

n = UserInt()
print n
m = UserInt(2)
print m
print n+m
print type(n) is types.IntType
print type(n)
