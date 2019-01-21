# Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros. 
# Print the decimal value of each fraction on a new line.


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos = 0
    nev = 0
    neu = 0
    num = 0

    for item in arr:
        num += 1

        if item > 0:
            pos += 1
        


        elif item < 0:
            nev += 1
        
    
        else:
            neu += 1

        a = pos/num
        b = nev/num
        c = neu/num
        
    print ("{0:.6f}".format(a))
    print ("{0:.6f}".format(b))
    print ("{0:.6f}".format(c))
    



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)