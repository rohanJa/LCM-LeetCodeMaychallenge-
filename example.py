t=int(input())
while(t>0):
    x = {}
    y = {}
    m = {}

    points = int(input())
    points = 4*points -1

    while(points>0):
        l = list(map(int,input().split()))

        if l[0] in x:
            x[l[0]].append(l[1])
            x[l[0]].sort()
        else:
            x[l[0]]=[l[1]]
            x[l[0]].sort()

        if l[1] in m:
            m[l[1]].append(l[0])
            m[l[1]].sort()
        else:
            m[l[1]]=[l[0]]
            m[l[1]].sort()            
        points-=1

    del_key=[]
    
    for k in x:  
        for b in x:
            if k!=b and b not in del_key and x[k] == x[b]:
                del_key.append(b)
                del_key.append(k)
                break
    print("Y is "+str(m))
    print("X before "+str(x))
    for k in del_key:
        x.pop(k)
    print("X after "+str(x))

    keyLeft=[]
    ans=2
    for k in x:
        if len(x[k])<2:
            ans=k
        keyLeft.append(x[k])
        #if else
    answer=''
    if len(keyLeft[0])>len(keyLeft[1]):
        answer = str(ans)+" "+str(list(set(keyLeft[0])-set(keyLeft[1]))[0])
    else:
        answer = str(ans)+" "+str(list(set(keyLeft[1])-set(keyLeft[2]))[0])
    
    print(answer)
    t-=1