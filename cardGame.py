t=int(input())
while(t>0):
    match = int(input())
    point=[0,0]
    totalPoint=[0,0]
    while(match>0):
        a,b =map(int,input().split())
        point[0]=0
        point[1]=0
        while(a!=0 or b!=0):
            point[0]+=a%10
            point[1]+=b%10
            a=int(a/10)
            b=int(b/10)
        match-=1
        if(point[0]>point[1]):
            totalPoint[0]+=1
        elif(point[0]<point[1]):
            totalPoint[1]+=1
        else:
            totalPoint[0]+=1
            totalPoint[1]+=1
    if(totalPoint[0]>totalPoint[1]):
        print(str(0)+" "+str(totalPoint[0]))
    elif(totalPoint[0]<totalPoint[1]):
        print(str(1)+" "+str(totalPoint[1]))
    else:
        print(str(2)+" "+str(totalPoint[1]))
    t-=1