#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    midSum = 0

    for i in range(1,len(arr)-1):
      midSum += arr[i]

    print(midSum + arr[0], midSum + arr[len(arr)-1])
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

