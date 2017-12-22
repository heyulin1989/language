#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
#include <tuple>

template<typename F, size_t... I, typename ... Args>
inline auto tuple_apply_impl(const F& f, const std::index_sequence<I...>&, const std::tuple<Args...>& tp)
{
    return f(std::get<I>(tp)...);
}

template<typename F, typename ... Args>
inline auto tuple_apply(const F& f, const std::tuple<Args...>& tp) -> decltype(f(std::declval<Args>()...))
{
  return tuple_apply_impl(f, std::make_index_sequence<sizeof... (Args)>{}, tp);
}

void test1(){
  std::vector<int> vec({1,2,3,4,5,6,7,8,9});
  //接受一个打印的Lambda表达式
  std::for_each(vec.begin(), vec.end(), [](auto i){ std::cout<<i<<std::endl;});
  //接受一个转换的Lambda表达式
  transform(vec.begin(), vec.end(), vec.begin(), [](int i){ return i*i; });

}

void test2(){
  auto f = [](int x, int y, int z) { return x + y - z; };
  //将函数调用需要的参数保存到tuple中
  auto params = std::make_tuple(1, 2, 3);
  
  //将保存的参数传给函数f，实现函数调用
  auto result = tuple_apply(f, params); //result is 0
  
}
int main(){
  test2();
}
