/***
 * 
Each time a cart has the option to turn (by arriving at any intersection), 
it turns left the first time, goes straight the second time, turns right
 the third time,


- create class name 'cart'

```c
Cart attribute
  int dx:
  int dy: 
  int state;
  int x,y; track coordinate on matrix
   if state == 1: turn left.(dx = -1)
   if state == 2: turn straight(dy = 1)
   if state == 3: turn right(dx = 1)
```

1. read input. store in matrix(150x150)
- matrix representation
  - `\/-|` = '1'
  - `+`    = '2' arbitary
  - `' '`(blank)  = '0' 
  - if see '<|>|v|^|'
    - then create a object Cart. at that coor 

2. So now we have. 
- one matrix of the map. 
- an Array list of 'Cart' object. 


3. main Algorithm
- Iterate through array list of object. update the coordinate of each object base on 'dx' and 'dy' attribute of each. by lookingat the map matrix
  - if object coor hit position with '2'(intersection) then update 'stage' attribute 
- If 2 object have same coordinate then exit return that coor


coor dinate:
turn left: angle += 90; 
----------------------------------> +x: (0 degree)
|
|
|
|
|
|           
|
|
|
v +y 
90(degree)
 */

#include <iostream>
#include <map>
#include <string>
#include <string.h>
#include <bits/stdc++.h> // stringstream
#include <algorithm>
#include <math.h>

using namespace std;


#define DEG2RAD(DEG) (DEG*M_PI/180.0)

enum Road{
  EMPTY=0,
  TURNBACK,// turn (\)
  TURNFOR,// turn(/)
  ROAD, 
  INTERSECT
};

class Cart{
  public: 
    int x=-1,y=-1;
    int dx=-1,dy=-1;
  
    void setSteering(int angle){

      this->steering = angle%360;//TODO: double check this. 
      this->dx = round(cos(DEG2RAD(this->steering)));// update velocity as well.  
      this->dy = round(sin(DEG2RAD(this->steering)));
      // cout << "set angle" << angle << "cos"<< cos(this->steering) << "sin" << sin(this->steering) << endl;
    }

    
    int getSteering(){
      return this->steering;
    }
    int getState(){return this->state;}
    void setState(){
      this->state = (this->state+1)%3;
    }
    void turnLeft(){setSteering(this->getSteering()-90);}
    void turnRight(){setSteering(this->getSteering()+90);}
    string toString(){
      return "Steering:"+to_string(this->getSteering())+";Coor:("+to_string(x)+","+to_string(y)+") vel: dx:"+to_string(dx)+", dy:"+to_string(dy)+" with state:"+to_string(this->state);
    }
    void updateCoor(vector< vector<Road> > board){//dx_: next move
      int steering_=0;
      int nextx = this->x + this->dx;
      int nexty = this->y + this->dy;  
      // cout << "dx" << this->dx <<"dy" << this->dy << endl;
      if((this->dx > 0 && board[nexty][nextx] == TURNBACK) || 
        (this->dy > 0 && board[nexty][nextx] == TURNFOR)  ||
        (this->dx < 0 && board[nexty][nextx] == TURNBACK)||
        (this->dy < 0 && board[nexty][nextx] == TURNFOR)){
          this->turnRight();
      }else if((this->dx > 0 && board[nexty][nextx] == TURNFOR)||
              (this->dy < 0  && board[nexty][nextx] == TURNBACK)||
              (this->dx < 0 && board[nexty][nextx] == TURNFOR)||
              (this->dy > 0   && board[nexty][nextx] == TURNBACK)){
        this->turnLeft();
      }else if(board[nexty][nextx] == INTERSECT){
        //it turns left the first time, goes straight the second time,
        // turns right the third time,
        if(this->getState() == 0) this->turnLeft();
        else if(this->getState() == 2) this->turnRight();
        this->setState();
      }
      // update next dx and dy. prevent runing out of road. 
      this->x = nextx, this->y = nexty;
    }
    bool operator <(const Cart& rhs) const{
      if(this->x != rhs.x) return this->x < rhs.x; 
      else                 return this->y < rhs.y;
    }
  private:
    
    int state = 0;
    int steering = 0;
};

vector<string> tokenize(string str, char delim);
void printVec(vector<Road> vec);
void strRemove(string str);
void printBoard(vector<vector<Road>> board);

/**
 * Check the list of carts. to see if there are matching coor. 
 * If there is return true(there are collision)
 * false ogtherwise. 
 * Challege check for repeated with O(n) times eand O(1) space
 */
Cart* findCollision(vector<Cart> carts){
  map<Cart, int> cartMap; 
  for(int i=0;i<carts.size();i++){
    if(cartMap.count(carts[i])){//if cart already exist in ap
      return &carts[i]; 
    }else{// add to the map 
      cartMap[carts[i]] = 1;
    }// end else 
  }// end for
  return NULL;
}// end findCollision

/**
 * This function update the state of the board 
 * return true if there are no collision. 
 * Otherwise, false
 */
bool updateBoard(vector<vector<Road>> board, vector<Cart> &carts){
  Cart *collision;
  for(int i=0;i<carts.size();i++){
    // make sure cart does not goes out of track.
    carts[i].updateCoor(board); 
    // there might be a collision while updating
    collision = findCollision(carts); 
    if(collision!=NULL){
      cout << "there is a collision at: "<< collision->toString()<<endl;
          return false;
    }
  }
  collision = findCollision(carts); 
  if(collision!=NULL){
    cout << "there is a collision at: "<< collision->toString()<<endl;
    return false;
  }else{
    return true;
  }
 
}
void printCart(vector<Cart> carts){
  for(int i =0;i<carts.size();i++){
    cout << carts[i].toString() << endl;
  }
}

int main(int argc, char** argv){
  string inputs;
  int size = 150;
  vector<vector<Road>> board(size, vector<Road> (size, EMPTY));
  // vector<vector<Road>> board(size, vector<Road> (size, EMPTY));
  int row = 0;
  vector<Cart> carts;
  //preprocessing
  while(getline(cin, inputs)){// or (cin >> inputs)
    for(int i=0;i<inputs.length();i++){
      Cart cart;
      if(inputs[i] == '\\')
        board[row][i] = TURNBACK;
      else if(inputs[i] == '/' )
        board[row][i] = TURNFOR;// road
      else if(inputs[i] == '-' | inputs[i] == '|' )
      board[row][i] = ROAD;// road
      else if(inputs[i] == '>'){
        cart.setSteering(0);
        cart.y = row;cart.x = i;
        board[row][i] = ROAD; 
        carts.push_back(cart);
      }else if(inputs[i] == '<'){
        cart.setSteering(180); 
        cart.y = row;cart.x = i;
        carts.push_back(cart);
        board[row][i] = ROAD;
      }else if(inputs[i] == 'v'){
        cart.setSteering(90);
        cart.y = row;cart.x = i;
        carts.push_back(cart);
        board[row][i] = ROAD;
      }else if(inputs[i] == '^'){
        cart.setSteering(270);
        cart.y = row;cart.x = i;
        carts.push_back(cart); 
        board[row][i] = ROAD;
      }else if(inputs[i] == '+')
        board[row][i] = INTERSECT;// 2 is special
    }// end for
    row++;
  }// end while
  // printBoard(board);

  //MAIN RUN===========
  while(updateBoard(board, carts));// if there is a coli
  return 0; 
}



/***************************PREPROCESSING FUNCTION********************/

void strRemove(string str, char remove){
  str.erase(std::remove(str.begin(), str.end(), remove), str.end());
}

void printVec(vector<Road> vec){
  for(int i=0;i<vec.size();i++){
    cout<< vec[i];
  }
  cout << endl;
}

void printBoard(vector<vector<Road>> board){
  cout << endl;
  for(int i=0;i<board.size();i++){
    printVec(board[i]);
  }
}

vector<string> tokenize(string line, char delim){
  vector<string> tokens; 
  stringstream check1(line); 
  string intermidiate;
  while(getline(check1, intermidiate, delim))
    tokens.push_back(intermidiate);
  return tokens;
}
/***************************PREPROCESSING FUNCTION********************/




