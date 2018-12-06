import sys 
import math 


'''
Visualize tool: https://stackoverflow.com/questions/47001426/draw-rectangles-in-a-cartesian-coordinate-system
Algorithm: 
Complexity: nlogn

'''

class Grid: 
    def __init__(self):
        self.o = [None]*2 # origin
        self.w = 0
        self.h = 0
    def __str__(self):
        return "%s %d %d"%(self.o, self.w, self.h)
    def __lt__(self, other):#sort ascending. 
        return self.o[0] < other.o[0]

claimRecord = {}

def overLap2Claim(claim1, claim2):# assume claim2.o[0] > claim1.o[0] with comparator in the class
    '''3case:
        https://stackoverflow.com/questions/3269434/whats-the-most-efficient-way-to-test-two-integer-ranges-for-overlap
        claim1: a 
        claim2: b
        case 1:w=a2 - b1
        a1-------------a2
            b1--------------b2
        case 2:w= 0
        a1---------a2
                        b1-----------b2
        case 3:w = b2-b1
        a1-----------a2
             b1----b2        
    '''
    #overlap in x-axis
    w =  min(claim1.o[0]+claim1.w, claim2.o[0]+claim2.w)- max(claim1.o[0],claim2.o[0]) 
    h = min(claim1.o[1]+claim1.h, claim2.o[1]+claim2.h) - max(claim1.o[1],claim2.o[1])
    grid = Grid()
    grid.o[0] = max(claim1.o[0],claim2.o[0])
    grid.o[1] = max(claim1.o[1],claim2.o[1])
    grid.w = w
    grid.h = h
    if(w < 0 or h < 0):
        return [None,0]
    return [grid, w*h]
'''
this function count the repeted claim from previous record of claim 
'''
def countFromRecord(grid):#Grid
    validCount = 0
    for r in claimRecord: 
        print("overlap ",overLap2Claim(r, grid))
        [_,lap] = overLap2Claim(r, grid)
        print('lab in ' , lap) 
        validCount -= lap
    print("valid count " , validCount)
    return validCount


'''
This function count the overlap inches of grid. main funciton of the program 
'''
def countOverlap(claims):
    overlap = 0
    i=0
    j =0
    while(j < len(claims) and i < len(claims)):
        if(i==j):
            i+=1
        elif(claims[i].o[0] < claims[j].o[0]+claims[j].w):
            [grid,lap] = overLap2Claim(claims[i], claims[j])
            print("lap",lap)
            if(lap > 0):# only count the claim once
                #decide whether valid count
                overlap += (lap + countFromRecord(grid))
                #claim the grid record 
                claimRecord.update({grid:1})
            i += 1 
        elif(claims[j].o[0]+claims[j].w <= claims[i].o[0]):
            j += 1
        print(claimRecord)
    return overlap
#//#1 @ 126,902: 29x28
if __name__  == '__main__': 
    inputs = ""
    # claimSize = 10 
    c = 0
    claims = []
    f = open("data.txt","w+")
    #preprocessing 
    while(True):
        grid = Grid() 
        try:  
            inputs = input().rstrip()
        except EOFError:
            break

        tokens = inputs.split(" ") 

        tokenize = tokens[2].replace(':','').split(",")
        grid.o[0] = int(tokenize[0])+1
        grid.o[1] = int(tokenize[1])+1


        tokenize = tokens[3].split('x') 
        grid.w = int(tokenize[0])
        grid.h = int(tokenize[1])
        
        claims.append(grid)

        # f.write("ctx.strokeRect(%d,%d,%d,%d);"%
        # (grid.o[0], grid.o[1],int(tokenize[0]), int(tokenize[1])))
        # f.write("\n");
        c += 1

    # for e in claims:
    #     print(e)
    # f.close();
    claims.sort()
    print("Total overlap grid is ", countOverlap(claims))

    print("check dict")
    for e in claimRecord:
        print(e)


    
    
        
    

    
