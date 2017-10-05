#coding:utf8
'''
thread和threads

thread: 提供多线程底层支持模块，以低级原始的方式来处理和控制线程，使用起来较为复杂
threading: 基于thread进行包装，将线程的操作对象化，在语言层面提供了丰富的特性

threading: 
1. 对于同步原语的支持更为完善和丰富。thread只支持thread.LockType, 
   threading支持Lock指令锁，RLock可重入指令锁，还支持条件变量Condition,信号量Semaphore,
   BoundedSemaphore以及Event事件
2. 在主线程和子线程交互上更为友好
'''

import threading, time, sys
class test(threading.Thread):

    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        print "%s delay for %s" % (self.name, self.delay)
        time.sleep(self.delay)
        c = 0
        while True:
            print "This is thread %s on line %s" % (self.name, c)
            c = c + 1
            if c == 3:
                print "End of thread %s" % self.name
                break


t1 = test('Thread 1', 2)
t2 = test('Thread 2', 2)
t1.start()
print "Wait t1 to end"
t1.join()
t2.start()
print "End of main"

'''
python3中已经不存在thread模块，thread模块在python3中被命名为_thread

'''
