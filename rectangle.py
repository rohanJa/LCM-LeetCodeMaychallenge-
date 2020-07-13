t=int(input())
while(t>0):
    x = {}
    y = {}

    points = int(input())
    points = 4*points -1

    while(points>0):
        l = list(map(int,input().split()))

        if l[0] in x:
            x[l[0]].append(l[1])
        else:
            x[l[0]]=[l[1]]

        if l[1] in y:
            y[l[1]].append(l[0])
        else:
            y[l[1]]=[l[0]]
        points-=1
    ans = ''
    for val in x:
        if(len(x[val])==1):
            ans=str(val)
    ans+=' '
    for val in y:
        if(len(y[val])==1):
            ans+=str(val)
    print(ans)
    t-=1