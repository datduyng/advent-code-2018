/**
 * --- Part Two ---
Confident that your list of box IDs is complete,
 you're ready to find the boxes full of prototype fabric.
The boxes will have IDs which differ by exactly one character
 at the same position in both strings. For example, given the following box IDs:
abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz
The IDs abcde and axcye are close, but they differ by two characters (the second and fourth)
. However, the IDs fghij and fguij differ by exactly one character, the third (h and u). Those 
must be the correct boxes.

What letters are common between the two correct box IDs?
 (In the example above, this is found by removing the differing character from either ID, producing fgij.)

this program cpmlexity: n^2

==ideal solution: O(nlogn)
1.read input. 
2.sort by lexicographic order 
3. iterate through the list the check the 2 consecutive if the diff is = 1
4. if don't see
    4.a reverse the string 
    4.b repeat step 2 and 3 

*/
#include <iostream>
#include <map>
#include <string>
#include <string.h>
#include <bits/stdc++.h>

using namespace std;

bool isDiffByOne(string str1, string str2){
    //TODO: check size
    int diffNum = 0; 
    for(int i=0;i<str2.length();i++){
        if(str1.at(i)!=str2.at(i)) diffNum++;
        if(diffNum > 1) return false;
    }
    return true;
}


int main(int argc, char** argv){
    string input;
    long count2=0, count3=0;
    vector<string> ids; 

    while(cin >> input){
        ids.push_back(input);
    }

    for(int i=ids.size()-1;i>=1;i--){
        for(int j=i-1;j>=0;j--){
            if(i==j) continue;
            if(isDiffByOne(ids[i], ids[j])){
                /*found right box id*/
                for(int r=0;r<ids[i].length();r++)
                    if(ids[i].at(r)==ids[j].at(r)) cout << ids[i].at(r);
            
            return 0;
            }
        }// end j
    }
  return 0; 
}
