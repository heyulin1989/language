#include <iostream>

int main(){
  auto lambda = [](auto x){return x;};
  std::cout << lambda("Hello generic lambda!") << std::endl;
  auto* pstr = "aldjf";
  auto str = std::string(pstr)+"bcd";
  std::cout << str << std::endl;
  return 0;
  
}
