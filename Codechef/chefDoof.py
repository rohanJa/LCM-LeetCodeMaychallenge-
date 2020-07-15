t = int(input())

while(t>0):
    
    n = int(input())

    arr = list(map(int, input().split()))
    flag=0
    for val in arr:
        if(val%2==0):
            print("NO")
            flag=1
            break
    if(flag==0):
        print("YES")
    
    t-=1