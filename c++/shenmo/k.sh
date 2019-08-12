id=`ps aux|grep demo_linux_threads |grep -v grep |awk '{print $2}'`
kill -9 $id
