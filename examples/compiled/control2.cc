#include <iostream>
using std::cout;
using std::endl;
int main()
{
  int a = 1;
  switch (a) 
  {
    case 1:
      cout << "a=1" << endl; 
      break;
    case 2:
      // do something
      break;
    default:
      cout << "hi" << endl;
  }
}
