#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):

    list_=[0 for i in range(0,n+2)]
    itre=len(queries)
    m=-1
    for query in queries:
        i=query[0]
        while(i<=query[1]):
            list_[i]=list_[i]+query[2]
            if(m<list_[i]):
                m=list_[i]
            i=i+1
        itre=itre-1

    return m

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
