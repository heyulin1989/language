#include <iostream>
#include <vector>
using namespace std;



template <typename T> class Foo{
public:
  static std::size_t count() { return ctr;}
  
private:
  static std::size_t ctr;
};

template <typename T> size_t Foo<T>::ctr = 3;

template<typename T>
void compare(T a, T b){
  cout << "tempate compare" << endl;
}
template<typename T, typename T1>
void compare(T a, T1 b){
  compare(a, b);
  cout << "tempate<T, T1>compare" << endl;
}

void compare(char* a, const char* b){
  cout << "compare" << endl;
}
int main(){
  char a = 'a';
  const char* p = &a;
  char* p1 = &a;
  compare(p, p1);
  return 0;
}
