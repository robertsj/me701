#include <iostream>
#include <fstream>
#include <string>
#include <vector>
int num_lines(std::string name){
 std::ifstream f(name.c_str());
 std::string line; int i = 0;
 for(;std::getline(f, line);++i)
  continue;
 return i;
}
int main(){
 int n = num_lines("data.txt");
 std::ifstream f("data.txt");
 std::vector<double> T(n),rho(n);
 for (int i = 0; i < n; ++i)
 {
  f >> T[i] >> rho[i];
  std::cout << T[i] << "\n";
 }
 f.close();
}
