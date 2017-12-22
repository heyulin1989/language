#include <iostream>
#include <vector>
using namespace std;

template<typename T> class Queue;
template<typename T> ostream& operator<<(ostream& os, const Queue<T>&);

template<typename Type>
class QueueItem{
  //public:
  // template<typename T> friend class Queue;
  friend class Queue<Type>;
  friend ostream& operator<< <Type> (ostream& os, const Queue<Type>&);
  QueueItem(const Type& t): item(t), next(0){ }
  Type item;
  QueueItem* next;
};


template<typename Type>
class Queue{
    friend ostream& operator<< <Type> (ostream& os, const Queue<Type>&);
public:
  Queue(): head(0), tail(0){}
  Queue(const Queue& Q):head(0), tail(0){ copy_elems(Q);}
  template<typename It>
  Queue(It beg, It end): head(0), tail(0){ copy_elems(beg, end);}
  Queue& operator=(const Queue&);
  ~Queue(){ destory();}
  Type& front(){ return head->item;}
  const Type& front() const { return head->item;}
  void push(const Type&); // add element to back of Queue
  void pop();// remove element from head of Queue
  bool empty() const{ return head == 0;}
  template <typename Iter> void assign(Iter, Iter);
  void test();
private:
  QueueItem<Type> *head;
  QueueItem<Type> *tail;
private:
  void destory();    // delete all the elements;
  void copy_elems(const Queue&);  // copy elements from parameter
  template <typename It> void copy_elems(It , It);  // copy elements from parameter
};

template<typename Type>
void Queue<Type>::destory(){
  while(!empty())
	pop();
}

template<typename Type>
void Queue<Type>::pop(){
  QueueItem<Type>* p = head;
  head = head->next;
  delete p;
}

template<typename T>
void Queue<T>::push(const T& val){
  QueueItem<T> *pt = new QueueItem<T>(val);
  if (empty()){
	head = tail = pt;
  }else{
	tail->next = pt;
	tail = pt;
  }
}

template<typename T>
void Queue<T>::copy_elems(const Queue& orig){
  for (QueueItem<T> *pt = orig.head; pt; pt = pt->next){
	push(pt->item);
  }
}
template<typename T>
template<typename Iter>
void Queue<T>::assign(Iter a, Iter b){
  destory();
  copy_elems(a, b);
}
template<typename T>
template<typename Iter>
void Queue<T>::copy_elems(Iter beg, Iter end){
  while(beg != end){
	push(*beg);
	++beg;
  }
}

template<typename T>
void Queue<T>::test(){
  for (QueueItem<T> *pt = head; pt; pt = pt->next){
	cout << "ele = " << pt->item << endl;
  }
}

template<typename T>
ostream& operator<<(ostream& os, const Queue<T>& q){
  for (QueueItem<T> *p = q.head; p; p = p->next){
	os << p->item << "\n";
  }
  return os;
}
void test1(){
  Queue<int> qi;
  for (int i = 0; i < 10; i ++){
	qi.push(i);
  }
  cout << qi;
}
void test3(){
  short a[4] = { 0, 4, 6, 9};
  Queue<int> qi(a, a+4);
  // vector<int> vi(a, a+4);
  // qi.assign(vi.begin(), vi.end());
  cout << qi;
}
void test2(){
  Queue<std::string> qstr;
  std::string tmp ;
  for (char c = 'A'; c <= 'z'; c++){
	tmp += c;
	qstr.push(tmp);
  }
  //qstr.test();
  cout << qstr;
}
int main(){
  //test1();
  //test2();
  test3();
  return 0;
}
