#your code goes here


def seive(a,b):
    prime = [True for i in range(0,b)]
    if(a==1):
        a=2
    p=2
    while(p*p<=b):
        if(prime[p]):
            for val in range(p*p,b,p):
                # print(val)
                prime[val]=False
        p+=1
    
    for i in range(a,b):
        if(prime[i]):
            print(i)
            
t=int(input())

while(t>0):
    a,b=map(int,input().split())
    seive(a,b+1)
    print()
    t-=1