#include <iostream>

class Query_base{
  friend class Query;
protected:
  typedef TextQuery::line_no line_no;
  virtual ~Query_base(){}
  virtual std::set<line_no> eval(const TextQuery& ) const = 0;
  virtual std::ostream& display(std::ostream& = std::cout) const = 0;
};

class Query{
  friend Query operator~(const Query&);
  friend Query operator|(const Query&, const Query&);
  friend Query operator&(const Query&, const Query&);
public:
  Query(const std::string&); 	//
  Query(const Query& c): q(c.q), use(c.use){++*use;}
  ~Query(){decr_use();}
  Query& operator=(const Query&);
  std::set<TextQuery::line_no> eval(const TextQuery& t) const { return q->eval(t);}
  std::ostream& display(std::ostream& os) const {return q->display(os);}
private:
  Query(Query_base *query):q(query),use(new std::size_t(1)){}
  Query_base *q;
  std::size_t *use;
  void decr_use(){
	if (0 == --*use){delete q; delete use;}
  }
};
inline Query operator~(const Query& oper){
  return new NotQuery(oper);
}
inline Query operator|(const Query& lhs, const Query& rhs){
  return new OrQuery(lhs, rhs);
}
inline Query operator&(const Query& lhs, const Query& rhs){
  return new AndQuery(lhs, rhs);
}


class WordQuery: public Query_base{
  friend class Query;
  WordQuery(const std::string& s): query_word(s){}
  std::set<line_no> eval(const TextQuery& t) const {
	return t.run_query(query_word);
  }
  std::ostream& display(std::ostream& os) const {
	return os << query_word;
  }
  std::string query_word;
};

class NotQuery: public Query_base{
  friend Query operator~(const Query&);
  NotQuery(Query q): query(q){}
  std::set<line_no> eval(const TextQuery&) const;
  std::ostream& display(std::ostream& os) const{
	return os << "~(" << query << ")";
  }
  const Query query;
};

class BinaryQuery: public Query_base{
protected:
  BinaryQuery(Query left, Query right, std::string op):
	lhs(left), rhs(right), oper(op){}
  std::ostream& display(std::ostream& os) const{
	return os << "(" << lhs << " " << oper << " " << rhs << ")";
  }
  const Query lhs, rhs;
  const std::string oper;
};


class AndQuery: public BinaryQuery{
  friend Query operator&(const Query&, const Query&);
  AndQuery (Query left, Query right):
	BinaryQuery(left, right, "&"){}
  std::set<line_no> eval(const TextQuery&) const;
};

class OrQuery: public BinaryQuery{
  friend Query operator|(const Query&, const Query&);
  AndQuery (Query left, Query right):
	BinaryQuery(left, right, "|"){}
  std::set<line_no> eval(const TextQuery&) const;
};

std::set<line_no> OrQuery::eval(const TextQuery& file) const{
  std::set<line_no> right = rhs.eval(file),
	ret_lines = lhs.eval(file);
  ret_lines.insert(right.begin(), right.end());
  
  return ret_lines;
}

std::set<TextQuery::line_no> AndQuery::eval(const TextQuery& file) const
{
  std::set<line_no> left = lhs.eval(fil),
	right = rhs.eval(file);
  std::set<line_no> ret_lines;
  std::set_intersetion(left.begin(), left.end(), right.begin(), right.end(),
						inserter(ret_lines, ret_lines.begin()));
  return ret_lines;
}
set<TextQuery::line_no>
NotQuery::eval(const TextQuery& file) const
{
  set<TextQuery::line_no> has_val = query.eval(file);
  set<line_no> ret_lines;
  // for each line in the input file, check whether that line is  in has_val
  // if not, add that line number to ret_lines
  for (TextQuery::line_no n = 0; n != file.size(); ++n)
	if (has_val.find(n) == has_val.end())
	  ret_lines.insert(n);
  return ret_lines;
}
