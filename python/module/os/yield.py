def g(n):
    for i in range(n):
        yield i ** 2

t = g(5)

#for i in t:
#    print i

a = [1, 2]
b = [3, 4]
a.extend(b)
print a
