import sys 
import math 

'''
treat #  : 1 
	  '.': 0
binary
'''
def findLeadingZero(plants):
	count = 0
	for x in plants:
		if(x == '0'):
			count+=1 
		else: return count
def print2D(thelist):
	 for item in thelist:
	 	print(item)

def plant_spread(plants , patterns):
	plants += "0000"
	spread = ""
	n = len(plants)
	spread += (plants[0]+plants[1])
	for i in range(2,n-2):
		pattern = ""
		#more efficient?? use dynamic programming. on this part 
		pattern += (plants[(i-2)]+plants[(i-1)]+plants[i]+plants[(i+1)]+plants[(i+2)])
		
		if(int(pattern,2) in patterns):
			# print(pattern,"to",patterns[int(pattern,2)])
			spread += patterns[int(pattern,2)]
		else: spread += '0'
	return spread
def billionGeneration(pattern='#...#...#...#...#...#...#...#...#.####...#...#...#...#...#...#...#...#...#...#...#...#...#...#...#...#...#..####...#...#...#...#...#...#...#...#...#...#...#...#...#...#...#..####'):
	indexes = []
	start = 5000000000-74#74: counted by eyeballing
	for index,x in enumerate(pattern):
		if(x == '#'): indexes.append(index+1)
	
	total = 0
	for i in indexes:
		total += (start+i)
	print((5000000000-83)*sum(indexes))
	return total 

if __name__  == '__main__': 
	patterns = {}
	initState = input().rstrip().split(' ')
	init = initState[2].replace('#','1').replace('.','0')
	while(True):
		try:  
			inputs = input().rstrip().split(' ')
			if(len(inputs[0])==0): continue
			texile = inputs[0].replace('#','1').replace('.','0')
			patterns[int(texile, 2)] = inputs[2].replace('#','1').replace('.','0')
		except EOFError:
			break
	print(len(init))
	print(init)
	print(patterns)
	next = init
	for gen in range(21):
		
		print('pattern',findLeadingZero(next),'gen',gen,next.replace('1','#').replace('0','.') )
		result = next[4:]
		next = plant_spread(next , patterns)
	
	#count all tree. 
	total = 0
	indexes = []
	print(result)
	for index, c in enumerate(result):
		if(c == '1'):
			indexes.append(index)
			total += (index)
	print(total)
	print(sum(indexes))

	print("billoon generation???" , billionGeneration())

	
'''
Part 2 no programming needed There should be a pattern at somepoint. 
Why? Let's take an example here. for example. You are the one who found the sine and cos function. 
You don't know the characteristic of it. You collect data and found that Every data point is a derivative of a 
cosine. Same idea in this case. If you take enough data point on the same set of derivative(all the LLCRR -> '') is the 
set of derivative of how the forest is changing. take that to the limit. there gotta be pattern at some point. 
converge at. '#...#...#...#...#...#...#...#...#.####...#...#...#...#...#...#...#...#...#...#...#...#...#...#...#...#...#..####...#...#...#...#...#...#...#...#...#...#...#...#...#...#...#..####'
265000000519 
[1, 5, 9, 13, 17, 21, 25, 29, 33, 35, 36, 37, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78, 82, 86, 90, 94, 98, 102, 106, 109, 110, 111, 112, 116, 120, 124, 128, 132, 136, 140, 144, 148, 152, 156, 160, 164, 168, 172, 175, 176, 177, 178]                           >>> start = 4999999918                                                                 >>> total = 0                                                                          >>> for i in indexes:                                                                  ...   total = (start+i)                                                                ...                                                                                    >>> total                                                                              5000000096                                                                             >>> for i in indexes:                                                                  ...   total = (start+i)                                                                ...   print(i)                                                                         ...             
'''