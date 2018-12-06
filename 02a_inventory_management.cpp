#include <iostream>
#include <map>
#include <string>
#include <string.h>
#include <bits/stdc++.h>

using namespace std;

//build frequency
map<char, int> buildFrequencyTable(const char* str){
  if(str == NULL){
    cout << "nothing in str(null)";
  }
  map<char, int> freqTable;
  for(int i=0;i<strlen(str);i++){
    freqTable[str[i]] += 1;
  }
  return freqTable;
}


int main(int argc, char** argv){
  string input;
  long count2=0, count3=0;
  

  while(cin >> input){
    bool have2 = false, have3 = false;
    map<char, int> freqTable = buildFrequencyTable(input.c_str());


    map<char, int>:: iterator it;
    for(it = freqTable.begin();it != freqTable.end();++it){// return then iterate
        cout << it->first << ":" << it->second << endl;
    }
    cout << endl;
    for(it = freqTable.begin();it != freqTable.end();++it){// return then iterate
        if(it->second == 2) have2 = true; 
        else if(it -> second == 3) have3 = true; 
    }
    if(have2)
      count2++;
    if(have3)
      count3++;
  }
  cout << "check sum of count2 and 3 is " 
       <<count2 << "," << count3 << "=" << count2*count3<< endl; 
  return 0; 
}
