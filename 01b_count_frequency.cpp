#include <iostream>
#include <map>
#include <string>
#include <string.h>
#include <sstream> // string split
#include <bits/stdc++.h>

using namespace std;

/**
 * To calibrate the device, you need to find the first frequency 
 * it reaches twice.
 */

int main(int argc, char** argv){
  //read all int line by line in file
  int num = 0;
  vector<int> nums;

  //preprocessing
  while( cin >> num){
    nums.push_back(num);
  }
  
  map<long, int> repeatFrequency; 
  repeatFrequency[0]++;
  long sum = 0;
  bool isCalibrated = false;
  while(!isCalibrated){
    for(int i=0;i<nums.size();i++){
        sum += nums[i];
        repeatFrequency[sum]++;
        if(repeatFrequency[sum]==2){// first reach twice
          cout << " first reach at: "<< sum << endl ;
          return 0;// isCalibrated = true;
        } 
      } 
  }
  
  // iterate through the map and find first frequency reach twice. 
  map<long, int>::iterator it; 
  for(it=repeatFrequency.begin();it!=repeatFrequency.end();++it){
    cout << it->first << " and " << it->second << endl;
  }
  return 0; 
}
