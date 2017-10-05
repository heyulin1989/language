#coding:utf8
'''
pickle: 数据序列化
cPickle是pickle速度的1000倍
pickle.dump(obj, file[,protocol]): 序列化数据到一个文件描述符
pickle.load(file): 从文件中的对象恢复为原来的对象，这个过程称为反序列化

限制:
1. pickle不能保证操作的原子性
2. pickle存在安全问题
3. pickle 协议是python特定的,不同语言之间的兼容性以难以保障
'''
import cPickle as pickle
my_data = {"name" : "Python", "type":"language", "version":"2.7.5"}
fp = open("picklefile.dat", "wb")  # 打开文件
pickle.dump(my_data, fp)
fp.close()

fp = open("picklefile.dat", "rb")
out = pickle.load(fp)
fp.close()
print(out)


'''
对于不可序列化的对象，如sockets,文件句柄，数据库连接，也可以通过实现pickle
协议来解决这些局限，主要通过特殊方法__getstate__()和__setstate__()方法
'''

class TextReader:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename)
        self.position = self.file.tell()
    def readline(self):
        line = self.file.readline()
        self.position = self.file.tell()
        if not line:
            return None
        if line.endswith('\n'):
            line = line[:-1]
        return "%i: %s" % (self.position, line)
    def __getstate__(self):          # 记录文件被pickle时候的状态
        state = self.__dict__.copy()     # 获取被pickle时的字典信息
        del state['file']
        return state
    def __setstate__(self, state):          # 设置反序列化后的状态
        self.__dict__.update(state)
        file = open(self.filename)
        self.file = file


reader = TextReader("zen.txt")
print(reader.readline())
print(reader.readline())
# 在dumps的时候会默认调用__getstate__
s = pickle.dumps(reader)
# 在loads的时候会默认调用__setstate__
new_reader = pickle.loads(s)
print(new_reader.readline())

