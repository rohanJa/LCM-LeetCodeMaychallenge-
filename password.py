#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    dict_={
        1 : "0123456789",
        2 : "abcdefghijklmnopqrstuvwxyz",
        3 : "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        4 : "!@#$%^&*()-+"
    }
    count=0
    for val in dict_:
        if(not bool(set(password).intersection(set(dict_[val])))):
            count=count+1
    
    if(6>len(password)+count):
        return (6-(len(password)+count)+count)
    else:
        count=0
        for val in dict_:
            if(not bool(set(password).intersection(set(dict_[val])))):
                count=count+1
        return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
