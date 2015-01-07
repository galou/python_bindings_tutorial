#include <python_bindings_tutorial/add_two_ints.h>

using namespace python_bindings_tutorial;

std_msgs::Int64 AddTwoInts::add(const std_msgs::Int64& a, const std_msgs::Int64& b)
{
  std_msgs::Int64 sum;
  sum.data = a.data + b.data;
  return sum;
}
