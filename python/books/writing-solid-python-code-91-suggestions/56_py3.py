#coding:utf8
def outside():
    msg = 'outside'
    def inside():
        #nonlocal msg
        msg = 'inside'
        def inside1():
            nonlocal msg
            msg = 'inside1'
            print (msg)

        inside1()
        print (msg)
    inside()
    print (msg)

outside()

