#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the theGreatXor function below.
def theGreatXor(x):

    a=str(bin(x))[2:]
    a=a[-1::-1]
    sum=0   
 
    for i,val in enumerate(a):
        if(val=='0'):
            sum=sum+pow(2,i)
 
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        x = int(input())
        result = theGreatXor(x)
        fptr.write(str(result) + '\n')

    fptr.close()
