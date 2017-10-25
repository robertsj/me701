#include <iostream>
using std::cout;
using std::endl;
int add(int a, int b)
{
  cout << "add ints" << endl;
  return a + b;
}
int add(double a, double b)
{
  cout << "add doubles" << endl;
  return a + b;
}
int main(int argc, char* argv[])
{
  cout << add(1, 2) << endl;
  cout << add(1.0, 2.0) << endl;
  return 0;
}
