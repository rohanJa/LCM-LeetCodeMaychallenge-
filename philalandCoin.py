n=int(input())
a=0 
while(a<n):
    num=int(input())
    noOfDigit = 0
    while(2**noOfDigit<=num):
        noOfDigit+=1
    a+=1
    print(noOfDigit)