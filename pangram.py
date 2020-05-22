#!/bin/python3
"pangram is when it contain all the character in english alphabets"
import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(s):
    s=s.lower()
    countChar={}
    for val in s:
        if val not in countChar and val != ' ':
            countChar[val]=1
    
    return "pangram" if(len(countChar)==26) else "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
