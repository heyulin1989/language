#include <iostream>
using namespace std;
class myclass
{
public:
  myclass(){} // 复制构造函数
  // myclass(const myclass &obj)
  // 	: age(obj.age),name(obj.name)
  // {} // 复制构造函数
  ~myclass(){} // 析构函数
  myclass& operator=(const myclass &obj){  // 赋值操作符
	age = obj.age;
	name = obj.name;
	return *this;
  }
  
  myclass& operator=(string str ){  // 赋值重载
	name = str;
	return *this;
  }
public:
  int age;
  string name;
};


// 测试复制控制
void test_1(){
  myclass	obj1;
  obj1.age = 2000;
  obj1.name = "john";

  //myclass	obj2(obj1);
  // 复制(拷贝)构造函数，是用一个已知的对象去初始化另一个正在创建的对象；赋值操作，是用一个已经存在的对象去更新另一个已经存在的对象。
    myclass	obj2 = obj1;  //  这个运行的复制构造函数
  //myclass obj2;
  //obj2 = obj1;
	obj2 = "kkkkkkkkkkk";
  cout << obj2.age << endl;
  cout << obj2.name << endl;
}


class curr
{
  friend class test;
private:
  curr(myclass *ip):cur(ip),used(1){};
  ~curr(){
	cout << "已经没有任何的指针指向myclass对象!" << endl;
	if (NULL != cur){
	  delete cur;
	}
  }
private:
  myclass *cur;
  int used;
};

class test{
public:
  test(myclass *ip, string stname, int stage)
	: pro(new curr(ip)), name(stname), age(stage){}
  test(const test& t): pro(t.pro), name(t.name), age(t.age){
	++ pro->used;
  }
  ~test(){
	--pro->used;
	if (!pro->used){
	  cout << "over" << endl;
	  delete pro;
	}
  }

  void show(){cout << pro->used << endl;}
private:
  curr* pro; // curr的对象
  string name;  // 名字
  int age;
};

void test_cur(){
  myclass *pr = new myclass();
  test *t1 = new test(pr, "tm", 21);
  t1->show();
  test *t2 = new test(*t1);
  t1->show();
  t2->show();

  delete t2;
  delete t1;
  
}


// 虚表，虚指针
class A{
public:
  virtual void vfunc1(){cout << "vfunc1" << endl;};
  virtual void vfunc2(){cout << "vfunc2" << endl;};
  virtual void vfunc3(){cout << "vfunc3" << endl;};

public:
public:
  int i;
  int j;
};

void test_vfunc(void){
  // cout << (*(this->vptr)[0]) << endl;
  // cout << (*(this->vptr)[1]) << endl;
  // cout << (*(this->vptr)[2]) << endl;
  void (A::*pfunc1)() = &A::vfunc1;
  void (A::*pfunc2)() = &A::vfunc2;
  void (A::*pfunc3)() = &A::vfunc3;

  cout << hex << &pfunc1 << endl;
  cout << hex << &pfunc2 << endl;
  cout << hex << &pfunc3 << endl;

}
typedef void (*func)();
int main(){
  A* p = new A();
  int* pvtbl = (int*)&(*p);
  func f = (func)*(int*)(*pvtbl);
  f();

  f();

  return 0;
}
