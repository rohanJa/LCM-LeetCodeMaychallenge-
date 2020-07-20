t = int(input())

while(t>0):
    strVal = list(input())
    strDict = {}
    
    for val in strVal:
        if val in strDict:
            strDict[val]+=1
        else:
            strDict[val]=1

    ch = strVal[0]
    count = 0
    for val in strDict:
        if strDict[val]>count:
            ch = val
            count = strDict[val]
        if strDict[val] == count and val < ch:
            ch = val
    ans=''
    for val in range(0,count):
        ans+=ch
    print(ans)
    t-=1