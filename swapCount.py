t = int(input())

while(t>0):
    s1 = int(input())
    s2 = int(input())
    l1 = list(map(int,input().split()))
    l2 = list(map(int,input().split()))
    d1 = {}
    d2 = {} 
    for val in l1:
        if val in d1:
            d1[val]+=1
        else:
            d1[val]=1

    for val in l2:
        if val in d2:
            d2[val]+=1
        else:
            d2[val]=1

    t-=1