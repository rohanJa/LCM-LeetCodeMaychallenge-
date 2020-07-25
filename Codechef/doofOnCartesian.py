t = int(input())



while(t>0):
    point = int(input())
    pointArray = list(map(int, input().split()))
    coOrdinate = int(input())
    
    while(coOrdinate>0):    
        x, y = map(int, input().split())
        flag = 0 
        countWall=0
        search(0, point, pointArray,x , y)
        for val in pointArray:
            a = y
            b = val-x
            if(a==b):
                print(-1)
                flag=1
                break
            if(x+y-val<0):
                print(countWall)
                flag=1
                break
            countWall+=1

        if(flag==0):
            print(countWall)
        coOrdinate-=1
    t-=1