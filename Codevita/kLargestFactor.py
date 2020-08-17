import math 
n,k = map(int,input().split())
l=[]
for i in range(1,int(math.sqrt(n))+1):
  if(n%i==0):
    k-=1
    l.append(i)
    if(k==0):
      answer=n//i
      break
if(k!=0):
  if(len(l)-k>=0):
    print(l[len(l)-k])
  else:
    print(1)
else:
  print(answer)