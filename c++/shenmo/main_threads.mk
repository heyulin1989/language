DIR=./shenmo-picture
NAME=demo_linux_threads
demo: ./main_threads.cpp
	/usr/bin/g++ -g ./main_threads.cpp  \
	-o ./$(NAME) \
	-I $(DIR)/include/ \
	-I $(DIR)/../ \
	-I $(DIR)/centos7/bin/thirdlib/opencv/opencv-2.4.10/include/ \
	-I $(DIR)/centos7/bin/thirdlib/gflag/include/ \
	-L $(DIR)/centos7/bin/thirdlib/opencv/opencv-2.4.10/lib -lopencv_highgui -lopencv_core -lpthread \
	-L$(DIR)/centos7/lib/ -lexport_sdk -lglog \
	-Wl,--rpath=$(DIR)/centos7/lib:$(DIR)/bin/lib:$(DIR)/centos7/lib/linux\
	-Wl,--rpath=$(DIR)/centos7/bin/thirdlib/opencv/opencv-2.4.10/lib:$(DIR)/centos7/bin/thirdlib/gflag/lib/linux/ \
	-D__LINUX__ \

all: demo

clean:
	/bin/rm -f ./$(NAME)
