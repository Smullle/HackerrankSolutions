#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    # better efficiency
    for i in range (d):
        over = a.pop(0)
        a.append(over)

    '''
    #uses too much memory
    for i in range (d):
        over = a[0]
        for i in range(len(a)-1):
            a[i] = a[i+1]
        a[len(a) -1] = over
    '''

    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
