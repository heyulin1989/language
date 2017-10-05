#coding:utf8
'''
logging模块

分为五个级别
Level:   DEBUG, INFO, WARNING, ERROR, CRITICAL

logging为线程安全，不支持多进程写入同一个日志文件
'''
import traceback
import sys
import logging

gList=['a', 'b', 'c', 'd', 'e', 'f', 'g']

logging.basicConfig(  # 配置日志的输出方式及格式
    level = logging.DEBUG,
    filename = 'log.txt',
    filemode = 'w',
    format = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
)

def f():
    gList[5]
    logging.info('[INFO]: calling method g() in f()')  # 记录正常的信息
    return g()
def g():
    logging.info('[INFO]: calling method h() in g()')
    return h()
def h():
    logging.info('[INFO]: Delete element in gList h()')
    del gList[2]
    logging.info('[INFO]: calling method i() in h()')
    return i()
def i():
    logging.info('[INFO]: calling method i() ')  # 记录正常的信息
    gList.append('i')
    print gList[7]
if __name__ == '__main__':
    logging.debug('Information during calling f():')
    try:
        f()
    except IndexError as ex:
        print "Sorry, Exception occured, you accessed an element out of range."
        #print ex()
        #print traceback.print_exc()
        ty,tv,tb = sys.exc_info()
        logging.error("[ERROR]: Sorry, Exception occured, you accessed an element out of range.")
        logging.critical('object info:%s' %ex)
        logging.critical('Error Type:{0}, Error Information:{1}'.format(ty, tv))
        # 记录异常的类型和对应的值
        logging.critical(''.join(traceback.format_tb(tb)))  #记录具体的trace信息
        sys.exit(1)
