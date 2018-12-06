#include <iostream>


using namespace std;

int main(int argc, char** argv){
  //read all int line by line in file
  int num = 0;
  long total; 
  while( cin >> num){
    total += num;
  }
  cout << "total is: " << total << endl;
  return 0; 
}
