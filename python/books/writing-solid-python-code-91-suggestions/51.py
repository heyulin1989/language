#coding:utf8
'''
模板方法模式: 一个方法中定义一个算法的骨架，并将一些实现步骤放延迟到子类中
'''
class People(object):
    def make_tea(self):
        teapot = self.get_teapot()
        teapot.put_in_tea()
        teapot.put_in_water()
        return teapot

class UseSimpleTeapot(object):
    def get_teapot(self):
        return SimpleTeapot()
class UseKungfuTeapot(object):
    def get_teapot(self):
        return KungfuTeapot()
def simple_tea_people():
    people = People()
    people.__bases__ += (UseSimpleTeapot, )
    return people
def caffee_people():
    people = People()
    people.__bases__ += (UseCoffeepot,)
def tea_and_coffee_people():
    people = People()
    people.__bases__ += (Usesimpleteapot, UseCoffeepot,)
def coffee_people():
    people = People()
    people.__bases__ += (UseSimpleTeapot, )
