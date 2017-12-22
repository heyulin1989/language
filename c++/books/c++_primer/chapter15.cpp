#include <iostream>
using namespace std;

class base{
protected:
  int pt_i;
};
class drive: public base{
public:
  void change_base_protect(int i){
	pt_i = i;
  }
  int get_i(){return pt_i;}
  
};
///  -------------------  书中的例子
class Item_base{
public:
  Item_base(const std::string &book = "",
			double sales_price = 0.0)
	:isbn(book), price(sales_price)
  {}
  std::string book() const {return isbn;}
  virtual double net_price(std::size_t n)  const {
	cout << "item_base" << endl;
	return n*price;
  }
  virtual void default_arg(int i = 100){
	cout << "item_base i = " << i << endl;
  }
private:
  std::string isbn;
protected:
  double price;
};

class Bulk_item: public Item_base{
public:
  double net_price(std::size_t) const;
  void default_arg(int i = 123){
	cout << "bluk_base i = " << i << endl;
  }

private:
  std::size_t min_qty;
  double discount;
};
double Bulk_item::net_price(std::size_t cnt) const{
  cout << "bluk_base" << endl;

  if (cnt > min_qty)
	return cnt * (1-discount)* price;
  else
	return cnt * price;
}

void print_total(ostream& os, const Item_base& item, size_t n){
  os << "ISBN: " << item.book()
	   << "\t number sold: " << n << "\ttotal price: "
	   << item.net_price(n) << endl;
}
///  -------------------  书中的例子

class change_private{
 public:
  // 在自己的类中可以直接操作private成员
  void change(change_private& a){
	a.i = 100;
  }
  void set_i(int i){ this->i = i;}
  int get_i(){return this->i;}
 private:
  int i;
  int j;
};
class test{
public:
  test(){

	//base_drive();
	//bluk_item();
	bluk_item_default_arg();
  }
  void bluk_item_default_arg(){
	// 虚函数的默认参数
	// 通过基类的引用或指针调用虚函数时,默认实参为在基类虚函数声明中指定的值,如果通过
	// 派生类的指针或引用调用虚函数,则默认实参是在派生类的版本中声明的值。
	Bulk_item derived;
	Item_base* p_base = &derived;
	Bulk_item* p_der = &derived;
	p_base->default_arg();
	p_der->default_arg();
  }
  void bluk_item(){
	Item_base base;
	Bulk_item derived;
	Item_base* p_base = &derived;
	print_total(cout, base, 10);
	print_total(cout, derived, 10);
	// 这个强制使用Item_base中的net_price;
	p_base->Item_base::net_price(42);
  }
  void base_drive(){
	drive dr;
	dr.change_base_protect(1);
	cout <<  dr.get_i() << endl;
	dr.change_base_protect(2);
	cout <<  dr.get_i() << endl;
  }
  void priv(){
	change_private t, c;
	t.set_i(12);
	c.change(t);
	cout << t.get_i() << endl;
  }
};


int main(int argc, char* argv[])
{
  test();
  return 0;
}
