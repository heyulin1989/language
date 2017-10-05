#coding:utf8
'''
使用trackback获取栈信息
'''

gList=['a', 'b', 'c', 'd', 'e', 'f', 'g']

def f():
    gList[5]
    return g()
def g():
    return h()
def h():
    del gList[2]
    return i()
def i():
    gList.append('i')
    print gList[7]
if __name__ == '__main__':
    try:
        f()
    except IndexError as ex:
        print "Sorry, Exception occured, you accessed an element out of range."
        print ex
