#include <iostream>
using namespace std;

class Base{
public:
  virtual void fun(){
	cout << "Base::fun" << endl;
  }
};

class D1 : public Base{
public:
  void fun(){cout << "D1::Base::fun" << endl;}
};

class D2 : public D1{
public:
  void fun(){cout << "D2::Base::fun" << endl;}
};

int main(){
  int p = 10;
  int*i = &p;
  ++*i;
  cout << "i = " << *i << endl;
  return 0;
}
