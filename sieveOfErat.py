# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
n=13

prime=[True for i in range(n+1)]
p=2
while(p*p<=n):
    if(prime[p]):
        for val in range(p*p,n+1,p):
            prime[val]=False
    p+=1
    
for val in range(2,n+1):
    if(prime[val]):
        print(val)
