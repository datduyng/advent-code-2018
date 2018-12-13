import sys 
import math 





'''
This algorithm attempt ot mimic the KNN machine learning algorithm 
1. Token list 
2. init matrix max and min base on coor 
3. iterate through the matrix 
	3.a compute the manhatan dist between each of point to all coors in list 
	3.b if No duplicate dis -> that spot of matrix = coor ID 
		else -> -1 

'''
def manhattan(x1,y1, x2,y2):
	return abs(x1-x2)+abs(y1-y2)

def anydup(thelist, key):
	count = 0 
	for x in thelist:
		if(int(key) is int(x)):
			count += 1
		if(count > 1):
			return True
	return False


def print2D(thelist):
	 for item in thelist:
	 	print(item)

if __name__  == '__main__': 
	manhattan_sum = 0# this track the sum less than 10000 for part 2
	coor = [] 
	inf = {} # keep track of infinite
	maxArea = {}#Python make this shit so simple.hash..hash.hash..
	while(True):
	    try:  
	        inputs = input().rstrip().split(',')
	    except EOFError:
	        break
	    coor.append([int(inputs[0]),int(inputs[1])])

	print(coor)
	COL = max(coor, key=lambda item:item[0])[0] # or max x 
	ROW = max(coor, key=lambda item:item[1])[1] # or max y
	size = max(COL,ROW)+1
	print("X", COL,"Y",  ROW)

	mat = [ [ -2 for i in range(size) ] for j in range(size) ]
	# mat = [[-2] *COL] * ROW
	print(len(mat[0]))


	## Part 2 
	for i in range(size):
		for j in range(size):
			nearestNeighbor = []
			for c in coor: 
				nearestNeighbor.append(manhattan(j,i,c[0],c[1]))		
			#for part 2
			if(sum(nearestNeighbor) < 10000): #10000 is a given value
				manhattan_sum += 1
		############

	##########################

	#iterate through and find min mahattan distance
	 
	# for i in range(len(mat)):
	# 	for j in range(len(mat[0])):
	# 		if ([j,i] in coor): 
	# 			mat[i][j] = coor.index([j,i])
	# 			continue
	# 		nearestNeighbor = []
	# 		for c in coor: 
	# 			nearestNeighbor.append(manhattan(j,i,c[0],c[1]))

	# 		minE = int(nearestNeighbor.index(min(nearestNeighbor)))
	# 		if(anydup(nearestNeighbor,min(nearestNeighbor))): 
	# 			mat[i][j] = -1 # if there is dup
	# 		else: 
	# 			mat[i][j] = minE
	# 			if(i == 0 or i == size-1 or j == 0 or j == size-1):
	# 				inf[minE] = 1# infinite grid
	
	# for i in range(size): 
	# 	for j in range(size):
	# 		if(mat[i][j] not in inf):
	# 			try: maxArea[mat[i][j]] += 1
	# 			except KeyError: maxArea[mat[i][j]] = 1
	# # print2D(mat)
	# print(inf)
	# print(maxArea)
	# #put into list and find maxxxx 
	# toList = [(value, key) for key, value in maxArea.items()]
	# print("your damn answer is ", max(toList))
	print("Part 2(Man hattan sum < 10,000 is" , manhattan_sum)

################
#####Test suit
################
# assert alchemReduction(inputs) == 'dabCBAcaDA'