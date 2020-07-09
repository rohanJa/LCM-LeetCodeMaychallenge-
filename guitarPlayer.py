t = int(input())

while(t>0):
    size = int(input())
    guitar = list(map(int,input().split())) 
    sGuitar = 0
    for i in range(0,len(guitar)-1):
        sGuitar+= abs(guitar[i]-guitar[i+1])-1
    t-=1
    print(sGuitar)