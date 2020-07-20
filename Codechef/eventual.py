t = int(input())

while(t>0):
    size = int(input())
    s = list(input())
    sDict = {}

    for val in s:
        if val in sDict:
            sDict[val]+=1
        else:
            sDict[val]=1
    flag=1
    for val in sDict:
        if(sDict[val]%2 != 0):
            flag=0
            break
    
    if(flag==1):
        print("YES")
    else:
        print("NO")
    
    t-=1