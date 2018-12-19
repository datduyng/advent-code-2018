#include <iostream>
#include <map>
#include <string>
#include <string.h>
#include <bits/stdc++.h> // stringstream
#include <algorithm>

/***
 * summed-area table Algorithm
 * 90, 57, 15
 */ 
using namespace std;

#define get_digit(number, n) (int(number / pow(10,n)) % 10) 

vector<string> tokenize(string str, char delim);
void strRemove(string str);
template <typename T> void printVec(vector<T> vec);
template <typename T> void print2dVec(vector<vector<T>> mat);


vector<vector<int>> fillPowerLevel(int size, int serial){
    vector<vector<int>> cells(size, vector<int> (size, 0));
    for(int i=0;i<size;i++){
        for(int j=0;j<size;j++){
        int y = i+1, x = j+1,
            rackID = x+10;
        long startPower = ((rackID * y)+serial)*rackID; 
        int firstDig = get_digit(startPower, 2); // get2nd digit
        int powerLevel = firstDig - 5;
        cells[y-1][x-1] = powerLevel; 
        }// end j 
    }// end i
    return cells;
}// end fillPowerLevel

int computeSqr(vector<vector<int>> mat, int row, int col, int sqSize){
  int result=0; 
  for(int i=row;i<row+sqSize;i++) 
    for(int j=col;j<col+sqSize;j++)
      result += mat[i][j]; 
  return result;
}

int maxSquare(vector<vector<int>> mat, int sqSize){
  int rows = mat.size(), cols = mat[0].size(); 
  int max = computeSqr(mat, 0,0,sqSize);
  vector<int> coor;// (X,Y) coordinate.correspond with (j,i)
  for(int i=0;i<rows-sqSize;i++)
    for(int j=0;j<cols-sqSize;j++){
      int sqr = computeSqr(mat,i,j,sqSize);
      if(sqr > max){
        max = sqr;coor = {j+1,i+1};
      }// end if
    }// end j
  cout << "Max begin Coor:";printVec(coor); 
  cout << "with max:" << max<< endl;
  return max;
}
int main(int argc, char** argv){
    /**
     * unit test
     * serial: 18 > 33,45 (with a total power of 29)
     * Serial: 42 > 21,61 (with a total power of 30)
     */ 
    int serial = 4455; //part 1 input 
    int size = 299; // range[1,300]
    vector<vector<int>> cells = fillPowerLevel(size, serial); 

    
    int squareSize = 3; 
    // cout << computeSqr(cells, 0,0,3)<< endl;
    // print2dVec(cels);
    
    maxSquare(cells, squareSize);

    return 0; 
}
/***********************PREPROCESSING*****************************/
void strRemove(string str, char remove){
  str.erase(std::remove(str.begin(), str.end(), remove), str.end());
}

template <typename T> void printVec(vector<T> vec){
  for(int i=0;i<vec.size();i++){
    cout<< vec[i]<<",";
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