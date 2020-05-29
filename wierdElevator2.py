# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import math
n=1000000

prime=[True for i in range(n+1)]
p=2

while(p*p<=n):
    if(prime[p]):
        for val in range(p*p,n+1,p):
            prime[val]=False
    p+=1

l1,l2,m=map(int,input().split())
print(str(l1)+" "+str(l2)+str(m))

gcd_lift = math.gcd(l1,l2)
print(gcd_lift)
l1_factor = int(l1/gcd_lift)
l2_factor = int(l2/gcd_lift)

time=0
for i in range(2,m+1):
    if(prime[i]):
        while(l1_factor%i==0):
            l1_factor=int(l1_factor/i)
            time+=1
        while(l2_factor%i==0):
            l2_factor=int(l2_factor/i)
            time+=1
        if(l1_factor==1 and l2_factor==1):
            break

if(l1_factor==1 and l2_factor==1):
    print(str(time)+" "+str(gcd_lift))
else:
    print("-1")