n=list(map(int,input().strip().split(' ')))
lastknown=len(n)-1

for i in range(len(n)-2,-1,-1):
    print("index "+str(i)+" "+str(n[i]))
    if(i+n[i]>=lastknown):
        lastknown=i

if(lastknown==0):
    print("YES")
else:
    print("NO")
