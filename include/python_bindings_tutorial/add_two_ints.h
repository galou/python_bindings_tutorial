#ifndef PYTHON_BINDINGS_TUTORIAL_ADD_TWO_INTS_H
#define PYTHON_BINDINGS_TUTORIAL_ADD_TWO_INTS_H

#include <std_msgs/Int64.h>

namespace python_bindings_tutorial {

class AddTwoInts
{
  public:
    std_msgs::Int64 add(const std_msgs::Int64& a, const std_msgs::Int64& b);
};

} // namespace python_bindings_tutorial

#endif // PYTHON_BINDINGS_TUTORIAL_ADD_TWO_INTS_H

