#coding:utf8
'''
Queue.Queue(maxsize): 先进先出，maxsize为队列大小，其值为非正数时为无限循环队列
Queue.LifoQueue(maxsize): 后进先出，相当于栈
Queue.PriorityQueue(maxsize): 优先级队列

Queue.qsize(): 返回近似的队列大小，当该值>0的时候并不保证并发执行的时候get()方法不被阻塞，
               同样对于put()方法有效
Queue.empty(): 为空返回True, 否则为False
Queue.full(): 队列满返回True, 否则为False
Queue.put(item[,block,[timeout]]):   队列满返回True,否则为False. block为False时，队列满则
        抛出Full异常。如果block为True, timeout为None的时候，则会一直等待直到有空位置，否则
        会根据timeout的设定超时后抛出Full异常。
Queue.put_nowait(item): 等价于put(item, False)
Queue.get([block[, timeout]]): 从队列中删除元素并返回该元素
Queue.get_nowait(): 等价于get(False)
Queue.task_done(): 发送信号表明入列任务已经完成
Queue.join(): 阻塞直到队列中所有的元素处理完毕

Queue本身能够保证线程安全，因此不需要额外的同步机制
'''
import Queue
import threading
import random

#writelock = threading.Lock()
# class Producer(threading.Thread):
#     def __init__(self, q, con, name):
#         super(Producer, self).__init__()
#         self.q = q
#         self.name = name
#         self.con = con
#         print "Producer " +self.name+" Started"

#     def run(self):
#         while 1:
#             #global writelock
#             #self.con.acquire()  # 获取锁对象
#             if self.q.full():   # 队列满
#                 with writelock: # 输出信息
#                     print "Queue is full, producer wait!"
#                 self.con.wait() # 等待资源

#             else:
#                 value = random.randint(0, 10)
#                 with writelock:
#                     print self.name + " put value " + self.name + ":" +str(value) + "into queue"
#             self.q.put((self.name+":"+str(value)))  # 放入队列中
#             self.con.notify()  # 通知消费者
#         self.con.release()     # 释放锁

# class Consumer(threading.Thread):
    
#     def __init__(self, q, con, name):
#         super(Consumer, self).__init__()
#         self.q = q
#         self.con = con
#         self.name = name
#         print "Consumer "+self.name+" started \n"

#     def run(self):
#         while 1:
#             global writelock
#             self.con.acquire()
#             if self.q.empty():
#                 with writelock:
#                     print "queue is empty, consumer wait!"
#                 self.con.wait()
#             else:
#                 value = self.q.get()
#                 with writelock:
#                     print self.name + "get value" + value + " from queue"
#                 self.con.notify()
#             self.con.release()

# if __name__ == "__main__":
#     q = Queue.Queue(10)
#     con = threading.Condition()
#     p = Producer(q, con, "P1")
#     p.start()
#     p1 = Producer(q, con, "P2")
#     p1.start()
#     c1 = Customize(q, con, "C1")
#     c1.start()        
    

class Producer(threading.Thread):
    def __init__(self, queue, name):
        threading.Thread.__init__(self)
        self.queue = queue
        self.name = name
    def run(self):
        while True:
            num = random.randint(0, 10)
            print self.name+" ==> "+str(num)
            self.queue.put(num)
class Customer(threading.Thread):
    def __init__(self, queue, name):
        threading.Thread.__init__(self)
        self.queue = queue
        self.name = name
    def run(self):
        while True:
            print self.name+" ==> "+str(self.queue.get())
            self.queue.task_done()
            
if __name__ == "__main__":
    q = Queue.Queue(10)
    p = Producer(q,"P1")
    p.setDaemon(True)
    p.start()
    # p1 = Producer(q,"P2")
    # p1.start()
    c1 = Customer(q,"C1")
    c1.setDaemon(True)
    c1.start()        
    c2 = Customer(q,"C2")
    c2.setDaemon(True)
    c2.start()        
    q.join()
