size=int(input())

s=list(str(input()))
temp=s.copy()

count=0
countA=0
for val in range(len(s)-2,-1,-1):
    if(s[val]=='-'):
        if(s[val+1]=='A'):
            s[val]='A'
            count+=1
    elif(s[val]=='B'):
        if(count%2==0):
            countA+=count//2
        else:
            countA+=(count//2)+1
        count=0
    elif(s[val]=='A'):
        count=0

c=0
for val in range(0,len(s)):
    if(s[val]=='A'):
        c+=1

ansA=c-countA
print("ansA "+str(ansA))
count=0
countB=0
s=temp.copy()
for val in range(1,len(s)):
    if(s[val]=='-'):
        if(s[val-1]=='B'):
            s[val]='B'
            count+=1
    elif(s[val]=='A'):
        if(count%2==0):
            countB+=count//2
        else:
            countB+=(count//2)+1
        count=0
    elif(s[val]=='B'):
        count=0
        
c=0

for val in range(0,len(s)):
    if(s[val]=='B'):
        c+=1
ansB=c-countB
print("ans B "+str(ansB))
if(ansA==ansB):
    print("Coalition government",end='')
elif(ansA>ansB):
    print("A",end='')
else:
    print("B",end='')