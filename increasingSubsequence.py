arr=list(map(int,input().split()))

l=[1]*len(arr)

for i in range(1,len(arr)):
    for j in range(0,i):
        if arr[i]>arr[j] and l[j]+1>l[i]:
            l[i]=l[j]+1
mac=-1
for i in range(0,len(arr)):
    mac=max(mac,l[i])
print(mac)