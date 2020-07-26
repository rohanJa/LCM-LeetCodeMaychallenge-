t = int(input())

while(t>0):
    n, m, x , y =  map(int,input().split())
    total=0
    row = n
    col = m

    if(n%2==0 or m%2==0):
        multi = (row*col)//2
        if(y-x<x):
            total+=(multi*y)
        else:
            total+=(row*col*(x))
    else:
        multi=((row-1)*(col))//2
        if(y-x<x):
            total+=(multi*y)
            total+=((col//2)*y)+(y-1) 
        else:
            total+=(row*col*(x))

    print(total)

    t-=1