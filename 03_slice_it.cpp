#include <iostream>
#include <map>
#include <string>
#include <string.h>
#include <algorithm>
#include <sstream> // string split
#include <bits/stdc++.h>


using namespace std;

struct Grid{
  int origin[2];//(p0,p1) 
  int x[2]; //p(p0,p1)
  int y[2];// (p0,p1)
};

void split(const string& s, char delim,vector<string>& v) {
    auto i = 0;
    auto pos = s.find(delim);
    while (pos != string::npos) {
      v.push_back(s.substr(i, pos-i));
      i = ++pos;
      pos = s.find(delim, pos);

      if (pos == string::npos)
         v.push_back(s.substr(i, s.length()));
    }
}

void removeChar(char *charToRemove, string &str){
  for(uint i =0; i< strlen(charToRemove);++i){
    str.erase(remove(str.begin(), str.end(), charToRemove[i]), str.end());
  }
  cout << str << endl; 
}


int main(int argc, char** argv){
  string inputs;
  int count = 0;
  const int n = 10;
  vector<Grid> claims;
  // preprocess data; 
  //#1 @ 126,902: 29x28
  while(cin >> inputs && count < n){
    cout << "cont "<< count << endl;
    Grid grid ;
    vector<string> tokens;
    split(inputs,' ', tokens);
    cout << " here " << endl;
    vector<string> originTokens; 
    cout << " remove " << tokens[0] << endl;
    cout << " her note " << endl;
    removeChar((char*)":", tokens[2]);

    
    split(tokens[2],',',originTokens);
    grid.origin[0] = stoi(originTokens[0]);
    grid.origin[1] = stoi(originTokens[1]);

    vector<string> gridSizeToken; 
    split(tokens[3], 'x', gridSizeToken);

    claims.push_back(grid);
    count ++;
  }

  for(int i=0;i<claims.size();i++){
    cout << claims[i].origin[0] << endl;
  }

  return 0; 
}
