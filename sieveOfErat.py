# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
n=int(input())

prime=[True for i in range(n+1)]
p=2
while(p*p<=n):
    if(prime[p]):
        for val in range(p*p,n+1,p):
            prime[val]=False
    p+=1
    
q=int(input("Enter number of queries "))

while q>0:
    a=int(input("Enter the number "))
    for val in range(2,a+1):
        if(prime[val]):
            print(val)
    q-=1
