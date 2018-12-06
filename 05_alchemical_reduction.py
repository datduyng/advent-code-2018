import sys 
import math 
import re



def alchemReduction(polymers):
    result =""
    for c in polymers:  
        if(len(result)==0):
            result += str(c)
        elif( ((result[-1].isupper() and c.islower()) or
               (result[-1].islower() and c.isupper())) and 
                result[-1].lower() == c.lower()):#end of the polymers
            result = result[:-1] #remove the last char: this is so inefficient though
            continue
        else:
            result += str(c)
    return result

def preventCollapse(polymers):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for a in alphabet:
        process = re.sub(a+"|"+a.upper(),"",polymers)
        reaction = alchemReduction(process)
        print("remove",a,"give:",len(reaction))

if __name__  == '__main__': 
    try:  
        inputs = input().rstrip()
    except EOFError:
        print("huh")

    #part 1
    # print('len of polymers ',len(alchemReduction(inputs)))

    #part 2
    preventCollapse(inputs)
    

################
#####Test suit
################
testSuit = ['dabAcCaCBAcCcaDA',
            'abAB',
            'LlspxXPjJMmBbVvyYNnzLlZFfSTtULRlLrTtbBlaAJjqQUuXxQnWwNqIiDiIdRIWwQqirWQqwfFlLiIeYyEJiIjjPHhpStTsJVTtvtjbBjuUJJZUuZzGgOoHhUumMYyoOBboVHZzhvsKkSspPZzFfTtScCOzkKfUxXLluLlRrFTyYSstuUJVvLljJjTqQCxXjJxVvCcwWVvXzJjyFfYleEUuAORroamMLRMmOorKkSNnsXxvVJjZOohHeELGglVGkKJjgvciIMeEvQqVmVvHgGKkhwWdDMmwbBrRrRWjrRJSCcoOPpkKepPjJEswaAfFVvWwfFpnNoDdOPpqVvFfHJJjjzZCmMvwWXxJjzkmMKZQqPzyYZHhKkAFfapgOoBbFAVvatTfGCyYTtcgGLlEerRFHhfIbVvBbBiFfNSsnDDddNnnfFjJtjJkKR',
            'LlspxXPjJMmBbVvyYNnzLlZFfSTtULRlLrTtbBlaAJjqQUuXxQnWwNqIiDiIdRIWwQqirWQqwfFlL']
# print(alchemReduction(inputs))
assert alchemReduction(testSuit[0]) == 'dabCBAcaDA'
assert alchemReduction(testSuit[1]) == 'abAB'
# print(alchemReduction(testSuit[2]))
# print(alchemReduction(testSuit[3]))
