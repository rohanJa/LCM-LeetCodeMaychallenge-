#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):

    visited = [False for i in arr]
    sum_=0
    for i in range(0,len(arr)):
        if(not visited[i]):
            a = i
            b = arr[i]-1
            len_=1
            visited[a]=True
            while(b!=i):
                visited[b]=True
                a=b
                b=arr[b]-1
                len_=len_+1
            len_=len_-1
            sum_=sum_+len_
    return sum_

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
