import sys 
import math 


if __name__  == '__main__': 
    try:  
        inputs = input().rstrip()
    except EOFError:
        break
    

################
#####Test suit
################
assert alchemReduction(inputs) == 'dabCBAcaDA'