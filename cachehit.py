# cook your dish here

t = int(input())
while(t>0):
    n,b,m = map(int,input().split())
    arr = list(map(int,input().split()))
    count = 1
    current = arr[0]//b
    for index in range(1,len(arr)):
        if arr[index]//b != current:
            current = arr[index]//b
            count+=1
    print(count)
    t-=1