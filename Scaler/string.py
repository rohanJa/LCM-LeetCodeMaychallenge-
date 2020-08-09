s = list("0100010010")

arr = [0 for i in range(len(s))]
if s[0]=='0':
    arr[0]=1
for i in range(1,len(s)):
    if(s[i] == '0'):
        arr[i]=arr[i-1]+1
    else:
        arr[i]=arr[i-1]

query = [1,8]
ans = []
smallest=-1
largest=-1
for i in range(query[0]-1,query[1]):
    if  s[i]=='1':
        if smallest==-1:
            smallest=i

        if largest<i:
            largest=i
print(largest)
print(smallest)
if largest!=-1 and smallest!=-1:
    ans.append(arr[largest] - arr[smallest])
else:
    ans.append(0)
print(ans)