#include "compare.hpp"

//export template<typename T, typename T1> T (*pcompare)(T1, T) = compare;
int main(){
  // 这个就失去了模型推断的意义
  //cout << pcompare<int, int>(1, 0) << endl;
  cout << compare(1, 0) << endl;
  cout << compare(3.14, 2.7) << endl;
  cout << compare(3.14, 2.7) << endl;
  cout << compare(3, 2.7) << endl;
  return 0;
}
