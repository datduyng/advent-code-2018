import math
import sys


def alpha2num(letter):
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	return alphabet.index(letter)
def num2alpha(index):
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	return alphabet[index]

'''
This function return true false if a node have meet the prere
to explore that node. True if Other node is ready to explore
'''
def prerequisite(adjMat, to, visited): 
	for n in range(26):
		if(adjMat[n][to]==1 and num2alpha(n) not in visited):
			return False
	return True

def findStartNode(adjMat):
	startNodes = set()
	for i in range(26): 
		count = 0 
		for j in range(26):
			if(adjMat[j][i]==1):
				count += 1 
		if(count == 0):
			startNodes.add(num2alpha(i))
	return startNodes



def printDict(mydict):
	for node in mydict:
		print("node",node, mydict[node])
def print2D(thelist):
	 for item in thelist:
	 	print(item)


def minWorkTime(worker): 
	min = len(worker[0])
	minArg = 0
	for index,w in enumerate(worker):
		if(min > len(w)):
			min = len(w)
			minArg = index
	return minArg 

'''
Space complexity of this problem can be reducce by using runlength coding
this function return time that n worker can acomplish the task. 
'''
def solveWithNWoker(adjMat,nodes , startList,n=2):
	print(adjMat)
	visited = set()
	worker = [[] for i in range(n)]
	working = {}
	print(startList)
	while(len(startList) != 0):
		count = 0 
		start = (sorted(startList))[count]
		while(not prerequisite(adjMat, alpha2num((sorted(startList))[count]),visited) ):
			count += 1
			start = sorted(startList)[count]
		
		#put the lazy worker to work. 
		minWork = minWorkTime(worker)
		if(len(worker[minWork])!=0): 
			try: 
				startList = startList.union( set(nodes[worker[minWork][0][-1:][0]]) )
				startList.remove(start)
			except KeyError:
				continue

		worker[minWork].append([start for i in range(alpha2num(start)+1)])
		working[start] = 1# a working queue kindof.
		
	
	for index, w in enumerate(worker):
		print("Worker ", index, "len", len(w))





if __name__  == '__main__': 
	nodes = dict()
	result = "" 
	adjMat = [ [ 0 for i in range(26) ] for j in range(26) ]
	while(True):
		try:  
			inputs = input().rstrip().split(' ')
		except EOFError:
			break

		fr = inputs[1]
		to = inputs[7] 
		try:
			nodes[fr].add(to)
		except KeyError:
			nodes[fr] = {to}# init set. So lame in python 
		adjMat[alpha2num(fr)][alpha2num(to)] = 1

	printDict(nodes)
	print2D(adjMat)


	startList = findStartNode(adjMat)
	print(startList)
	# result += str(min(startList))
	visited = set()

	while(len(startList)!=0):
		# print(startList, " visted" ,visited, "r:",result )
		count = 0
		# print(prerequisite(adjMat, alpha2num((sorted(startList))[count]),visited))
		
		start = (sorted(startList))[count]
		#get next available
		while(not prerequisite(adjMat, alpha2num((sorted(startList))[count]),visited) ):
			count += 1
			start = (sorted(startList))[count]
		#TODO: remove duplicate
		
		if(start not in visited):
			visited.add(start)
			result += str(start)
		# else: 
		# 	continue
		try:#The last element does not hold any child
			startList.remove(start)
			startList = startList.union(nodes[start])
		except KeyError: 
			continue
		
		# print(startList, "and" , nodes[start])
	print("with one worker", result)

	'''starting part 2'''
	startList = findStartNode(adjMat)
	solveWithNWoker(adjMat, nodes , startList)




################
#####Test suit
################
# assert alchemReduction(inputs) == 'dabCBAcaDA'
# ['C', 'E', 'H', 'Q', 'R']
