#nohup `pwd`/demo_linux_threads -auth_server=10.30.26.254:12821 -device=1,2,3 -thread_num=6,5,5 -i=./all.lst & 
#nohup `pwd`/demo_linux_threads -auth_server=10.30.26.254:12821 -device=0,1,2,3 -thread_num=5,5,5,5 -n=8 -i=./file.lst  -param_file=./param.txt &
#nohup `pwd`/demo_linux_threads -auth_server=10.30.26.254:12821 -device=0,1 -thread_num=5,5 -n=8 -i=./file.lst  -param_file=./param.txt &
nohup `pwd`/demo_linux_threads -auth_server=10.30.26.254:12821 -device=0 -thread_num=1 -n=1 -i=./file.lst  -param_file=./param.txt &


#nohup `pwd`/demo_linux_threads -auth_server=10.30.26.254:12821 -i=../../image -output=../../image -thread_num=1 &
