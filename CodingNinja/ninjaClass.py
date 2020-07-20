import math

def factor(n):
    maxFactor = 1
    for i in range(2,int(math.sqrt(n))+1):    
        if(n%i==0):
            if(i!=1 and maxFactor<int(n/i)):
                maxFactor = int(n/i);  
    print('n '+str(n)+' maxFactor '+str(maxFactor))
    return maxFactor

t = int(input())

while(t>0):
    n = int(input())
    val = []

    for i in range(0,n):
        val.append(int(input()))

    ans = []

    for i in range(1,n+1):
        # ans.append(factor(i))
        j=factor(i)-1
        print('i '+str(i)+' j '+str(j))

        if(i-1!=j):
            print('val '+str(val[j]))
            val[i-1] += val[j]

    for i in range(0,n):
        print(val[i],end=' ')

    print()    

    t-=1