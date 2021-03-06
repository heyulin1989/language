#encoding=utf-8
import os


def get_total_picture(path, picture_suffix):
    """ 
    功能:  得到当前目录下的图片数量
    参数:
        path:   图片所在的文件目录
        picture_suffix:   所要查找的图片的后缀
                          * : 代表所有
                          (下面功能没有实现)
                          .jpg   : 
     """
    total_picture = 0
    
    for parent,parent_folder,filenames in os.walk(path):
        count = len(filenames)
        if picture_suffix == '*':
            total_picture += count
            continue
        """
        for filename in filenames:
            if picture_suffix == '.jpg':
                total_picture += 1
        """

    return total_picture

if __name__ == '__main__':
    print get_total_picture('/home/heyulin/Desktop/pic','*')
