#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the xorSequence function below.
def xor(n):
    a=n%8
    if(a==0 or a==1):
        return n
    elif(a==2 or a==3):
        return 2
    elif(a==4 or a==5):
        return n+2
    elif(a==6 or a==7):
        return 0
    return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        lr = input().split()

        l = int(lr[0])

        r = int(lr[1])

        result = xor(r)^xor(l-1)

        fptr.write(str(result) + '\n')

    fptr.close()

    
