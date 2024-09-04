"""Module providing a function printing python version."""

import sys
import random
#import math

def generate_permutations(a, n):
    '''first task + modified'''
    # provide context, that counter is a global variable, and not a local,
    # and this way it is linked with the value defined outside the function
    global counter 
    
    if n == 0:
        rand = random.randrange(0,2)
        #print(counter)
        if rand and counter < 20:
            print(''.join(a))
            counter +=1
        
            
            
    else:
        for i in range(n):
            generate_permutations(a, n-1)
            j = 0 if n % 2 == 0 else i
            a[j], a[n] = a[n], a[j]
        generate_permutations(a, n-1)
    
    

if len(sys.argv) != 2:
    sys.stderr.write('Exxactly one argument is required\n')
    sys.exit(1)

word = "Iskren"
word = sys.argv[1]
counter = 0 # this anoys me a lot !!!!
  
generate_permutations(list(word), len(word)-1)

# py task1.py 'iskrenn'