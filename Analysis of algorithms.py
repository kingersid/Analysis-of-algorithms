
import time

# sum of N numbers

def sumOfN2(n):
   start = time.time()

   theSum = 0
   for i in range(1,n+1):
      theSum = theSum + i

   end = time.time()

   return theSum,end-start

sumOfN2(80)

# O(n) algo for finding min in a list
def minimum_in_list(x):
    minimum = x[0]
    for element in x[1:]:
        if element < minimum:
            minimum = element
    return minimum
        
#O(n^2) algo for find min in a list
def min_in_list(x):
    overall_min = x[0]
    for i in x:
        isminimum = True
        for j in x:
            if j < i:
                isminimum = False
            if isminimum:
                overall_min = i
    return overall_min
    

from random import randrange
import time

for listSize in range(1000,10001,1000):
    alist = [randrange(100000) for x in range(listSize)]
    start = time.time()
    print min_in_list(alist)
    end = time.time()
    print "size:",listSize," ~~~~~ " ,"time:",end-start




