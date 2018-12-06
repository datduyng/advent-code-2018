#include <iostream>
#include <map>
#include <string>
#include <string.h>
#include <bits/stdc++.h> // stringstream
#include <algorithm>

using namespace std;

vector<string> tokenize(string str, char delim);
void printVec(vector<string> vec);
string strRemove(string str, char remove);

class Soldier{
    public: 
      vector< vector<int> > sleeps; 
      int totalSleep = 0;
      string toString(){
        string result = ""; 
        for(int i=0;i<this->sleeps.size();i++){
          result += ("("+to_string(sleeps[i][0])+","+to_string(sleeps[i][1])+")");
          // result += (to_string(sleeps[i][1])+","); 
        }
        result += "\n" "Total sleep: "+ to_string(this->totalSleep);
        return result;  
      } 
      bool operator<(const Soldier & other) const{
        return this->totalSleep > other.totalSleep;
      }
    private:
};


/**
 * Main
 * This function attempt to find the max interval efficiently in 
 * O(n) time assuming that the given interval are sorted by starting time
 */
int overlappingIntervalsEfficient(vector< vector<int> > interval){
  int i=0,j=0;
  int currOverlap = 0, maxOverlap = 0;
  int sleepAt = 0; // keep track of the moment when the soldier start sleep

  if(interval.size()==1) return interval[0][0];

  while(i<interval.size() && j < interval.size()){
    if(interval[i][0] < interval[j][1]){
      currOverlap++;
      
      if(currOverlap > maxOverlap){
        sleepAt = interval[i][0];
      }
      maxOverlap = max(currOverlap, maxOverlap);
      i++;// increament entering time
    }else{
      j++;// increament leaving time 
      maxOverlap = max(currOverlap, maxOverlap);
      currOverlap --;
    } 
  }// end while
  cout << "max over lap" << maxOverlap << endl;
  return sleepAt;
}// end overlappingIntervalEfficient


Soldier findMaxInMap(map<int, Soldier> m){
  long max = m.begin()->second.totalSleep;
  map<int, Soldier>:: iterator it;
  Soldier target = m.begin()->second;
  int targetID = 0;
  for(it = m.begin();it != m.end();++it){// return then iterate
    cout <<"ID:"<<it->first <<"sleep:"<< it->second.totalSleep << endl;
    if(it->second.totalSleep > max){
      max = it->second.totalSleep;
      target = it->second;
      targetID = it->first;
    }
  }
  cout << "target ID is "<< targetID << endl;
  return target;
}

int cmpByStartSleep(const vector<int>a, const vector<int> b){
  return a[0] < b[0];// ascending
}

int main(int argc, char** argv){
  string inputs;
  vector<string> tokens;
  map<int, Soldier> reposeRecord;// int: guard #, 

  int key=0 ,begin =0; 
  //preprocessing
  while(getline(cin, inputs)){// or (cin >> inputs)
    tokens = tokenize(inputs,']');
    vector<string> times = tokenize(tokenize(tokens[0],' ')[1],':');
    vector<string> states = tokenize(tokens[1],' ');

    //process
    if(states[1].compare("Guard")==0){
        key = stoi(strRemove(states[2],'#'));
        if(reposeRecord.find(key) == reposeRecord.end()){// if not found iin record 
            Soldier s;
            reposeRecord[key] = s;
        }
        if(stoi(times[0])!=0) begin = 0; 
        else begin = stoi(times[1]);
    }else if(states[1].compare("wakes")){
        begin = stoi(times[1]);
    }else if(states[1].compare("falls")){
        reposeRecord[key].sleeps.push_back(vector<int>{begin, stoi(times[1])});// inclusive end 
        reposeRecord[key].totalSleep += (stoi(times[1]) - begin);
    }
  }

  // map<int, Soldier>:: iterator it;
  // for(it = reposeRecord.begin();it != reposeRecord.end();++it){// return then iterate
  //   cout << it->first << endl; 
  //   cout << it->second.toString() << endl; 
  // }

  cout << "Target is " << endl; 
  Soldier target = findMaxInMap(reposeRecord); 
  cout << target.toString() << endl;

  sort(target.sleeps.begin(), target.sleeps.end(), cmpByStartSleep);
  cout << "after sort" << endl;
  cout << target.toString() << endl;

  cout << "Sleep at:"<< overlappingIntervalsEfficient(target.sleeps) << endl;
  return 0; 
}

string strRemove(string str, char remove){
  string result = str;
  result.erase(std::remove(result.begin(), result.end(), remove), result.end());
  return result;
}

void printVec(vector<string> vec){
  for(int i=0;i<vec.size();i++){
    cout << "\'"<< vec[i]<<"\',";
  }
  cout << endl;
}

vector<string> tokenize(string line, char delim){
  vector<string> tokens; 
  stringstream check1(line); 
  string intermidiate;
  while(getline(check1, intermidiate, delim))
    tokens.push_back(intermidiate);
  return tokens;
}