# Difference of sum of diagonals of a matrix


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    d1 = 0
    d2 =0
    for i in range(len(arr[0])):
        d1 += arr[i][i]
        d2 += arr[i][len(arr[0])-i-1]
        res = abs(d1 - d2)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()