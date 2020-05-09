#!/bin/python

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    e=int(b**0.5) #last squareeoot value
    s=a**0.5 #first assumed squareroot value
    if s-int(s) == 0:
        s-=1
    s=int(s)
    return e-s



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        ab = raw_input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()

