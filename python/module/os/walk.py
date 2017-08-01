#coding=utf-8
import os
import random
path = "../../"

""" 
这个walk将对于path下的所有文件及文件夹进行递归search
"""
for parent,parent_folder,filenames in os.walk(path):
    """ 这个为什么排序 """
    parent_folder.sort()

    """ 对文件进行排序 """
    filenames.sort()
    #print len(filenames)
    # random.seed(2)
    # random.shuffle(filenames)
    for filename in filenames:
        print parent
        print filename
