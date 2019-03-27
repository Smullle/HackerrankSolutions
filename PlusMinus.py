#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    length = len(arr)
    zeros, pos, neg = 0, 0, 0

    for i in range (length):
        if(arr[i] == 0):
            zeros += 1
        elif(arr[i] > 0):
            pos += 1
        elif(arr[i] < 1):
            neg += 1
        
    print(float(pos/length))
    print(float(neg/length))
    print(float(zeros/length))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

