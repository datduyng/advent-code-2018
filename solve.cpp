#include <iostream>
#include <map>
#include <string>
#include <string.h>
#include <bits/stdc++.h> // stringstream
#include <algorithm>

using namespace std;

vector<string> tokenize(string str, char delim);
void strRemove(string str);
template <typename T> void printVec(vector<T> vec);
template <typename T> void print2dVec(vector<vector<T>> mat);



int main(int argc, char** argv){
  string inputs;
  
  //preprocessing
  while(getline(cin, inputs)){// or (cin >> inputs)
    vector<string> tokens = tokenize(inputs,'');
  }

  return 0; 
}


/***********************PREPROCESSING*****************************/
void strRemove(string str, char remove){
  str.erase(std::remove(str.begin(), str.end(), remove), str.end());
}

template <typename T> void printVec(vector<T> vec){
  for(int i=0;i<vec.size();i++){
    cout << "\'"<< vec[i]<<"\',";
  }
  cout << endl;
}

template <typename T> void print2dVec(vector<vector<T>> mat){
    for(int i=0;i<mat.size();i++) printVec(mat[i]);
}

vector<string> tokenize(string line, char delim){
  vector<string> tokens; 
  stringstream check1(line); 
  string intermidiate;
  while(getline(check1, intermidiate, delim))
    tokens.push_back(intermidiate);
  return tokens;
}

/****************************PREPROCESSING**********************/