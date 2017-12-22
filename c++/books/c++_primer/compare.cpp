#include "compare.hpp"
export template<typename T, typename T1> T compare(T1 a, T b){
  static int i = 0;
  cout << "function => "<< typeid(a).name() << typeid(b).name()  << "  "<<  i++ << endl;
  return a+b;
}
