arr=list(map(int ,input().split()))
max_number=-11
l=[1 for i in range(0,len(arr))]
for i in range(0,len(arr)):
    for j in range(0,i):
        if arr[i] >arr[j] and l[j]+1>l[i]:
            l[i]=l[j]+1
    print(l)
for j in range(0,len(l)):
    if(max_number<l[j]):
        max_number=l[j]
print(max_number)
