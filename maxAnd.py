import math 
t = int(input())

while (t>0):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    count = [ 0 for i in range(0,9)]
    for val in arr:
        temp=val
        index=0
        while(temp!=0):
            if(temp|1==1):
                count[index]+=1
            temp>>=1
            index+=1

    indexList=[]
    for z in range(0,k): 
        ind=0
        largest=0
        for i,val in enumerate(count):
            if i not in indexList:
                if val!=0 and largest<val:
                    largest=val
                    ind=i
        if(largest!=0):
            indexList.append(ind)
    s=''
    for i in range(0,9):
        if i in indexList:
            s='1'+s
        else:
            s='0'+s
    print(int(s,2))
    t-=1
