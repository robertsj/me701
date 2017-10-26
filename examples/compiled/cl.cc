#include <iostream>
#include <string>
#include <sstream>
using namespace std;
int main(int argc, char* argv[])
{
 if (argc != 2) 
 {
  cout << "usage: " << argv[0] 
       << " <arg>" << endl;
 }
 else 
 {
  std::string s = argv[1];
  cout << "arg = " << s << endl;
  int n = 1;
  if (!(istringstream(s) >> n)) 
    n = 0;
  cout << "n = " << n << endl;
 }
 return 0;
}
