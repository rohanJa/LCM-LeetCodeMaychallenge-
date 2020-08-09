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
    

seive()
a, b =list(map(int,input().split()))
firstPrime=[]
for val in range(a,b+1):
    if(prime[val]):
        firstPrime.append(val)
secondPrime = []
for i in firstPrime:
    for j in firstPrime:
        if(i!=j):
            val=int(str(i)+str(j))
            if(prime[val] and val not in secondPrime):
                secondPrime.append(val)
print(len(secondPrime))
a=[193, 3137, 197, 2311, 3719, 73, 137, 331, 523, 1931, 719, 337, 211, 23, 1117,223, 1123, 229, 37, 293, 2917, 1319, 1129, 233, 173, 3119, 113, 53, 373, 311, 313, 1913, 1723,317]
d={}
for val in secondPrime:
    if val in d:
        d[val]+=1
    else:
        d[val]=1
a=min(secondPrime)
b=max(secondPrime)
for i in range(len(secondPrime)-2):
    c=a+b
    a=b
    b=c
print(c)
print(d)