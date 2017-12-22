#include <iostream>
using namespace std;
class things
{
public:
  // 抑制隐式类型转化
  explicit things(const std::string&name =""):
	m_name(name),height(0),weight(10){}
  
  int CompareTo(const things & other){};
  std::string m_name;
  int height;
  int weight;
};

int main(){
  things a;
  const std::string str="kk";
  // 这里发生隐式类型转化
  int result = a.CompareTo(str);
  return 0;
}
