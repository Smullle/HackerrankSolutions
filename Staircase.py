#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    curr = 1

    for i in range(n-1):
      print(" " * (n-curr-1), "#" * curr)
      curr += 1

    print("#" * n)

if __name__ == '__main__':
    n = int(input())

    staircase(n)

