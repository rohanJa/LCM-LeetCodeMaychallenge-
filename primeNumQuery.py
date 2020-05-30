#!/bin/python3

import sys
prime=[True for i in range(0,1000000+1)]

def seive():
    
    n=1000000
    p=2
    prime[0]=False
    prime[1]=False
    while p*p<=n:
        if(prime[p]):
            for i in range(p*p,n+1,p):
                prime[i]=False
        p+=1
def maxDifference(startVal, endVal):
    # Complete this function

    a=-1
    for i in range(startVal,endVal+1):
        if(prime[i]):
            a=i 
            break
    # print("a "+str(a))
    
    if(a==-1):
        return 0
    b=-1
    for i in range(endVal,startVal-1,-1):
        if(prime[i]):
            b=i 
            break
    # print("b "+str(b))
    if(b==-1):
        return 0

    return (b-a)
if __name__ == "__main__":
    seive()
    q = int(input().strip())
    for a0 in range(q):
        startVal, endVal = input().strip().split(' ')
        startVal, endVal = [int(startVal), int(endVal)]
        result = maxDifference(startVal, endVal)
        print(result)