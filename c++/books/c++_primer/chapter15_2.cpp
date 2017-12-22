#include <iostream>
using namespace std;
class Sales_item{
public:
  double net_price(int i){return 0;}
private:
  
};

class Basket{
  typedef bool (*Comp)(const Sales_item&, const Sales_item&);
public:
  typedef std::multiplies<Sales_item, Comp> set_type;
  typedef set_type::size_type  size_type;
  typedef set_type::const_iterator const_iter;
  Basket(): items(compare){}
  void add_item(const Sales_item& item){items.insert(item);}
  size_type size(const Sales_item& i) const {return items.count(i);}
  double total() const;
private:
  std::multiplies<Sales_item, Comp> items;
};


double Basket::total() const{
  double sum = 0.0;				// holds the running total
  /*
	find each set of items with the same isbn and calculate
	the net price for that quantity of  items
	iter refers to first copy of each book in the set upper_bound
	refers to next element with a different isbn
   */
  for (const_iter iter = items.begin();
	   iter != items.end(); iter = iterms.upper_bound(*iter)){
	sum += (*iter)->net_price(items.count(*iter));
  }
  return sum;
}

class test_multiplies{
public:
  typedef bool (*Comp)(const int&, const int&);
  typedef set_type::size_type  size_type;
  typedef set_type::const_iterator const_iter;
  size_type size(const int& i) const {return items.count(i);}
  void add(const int& i){items.insert(i);}
private:
  std::multiplies<int, Comp> items;
};

int main(){
  test_multiplies t;
  int i = 0;
  t.add(i);
  cout << "i count = " << t.size(i) << endl;
  t.add(i);
  cout << "i count = " << t.size(i) << endl;
  t.add(i);
  cout << "i count = " << t.size(i) << endl;
  t.add(i);
  cout << "i count = " << t.size(i) << endl;
  return 0;
}
