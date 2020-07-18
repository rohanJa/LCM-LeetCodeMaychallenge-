n = int(input())
bride = list(map(str,input()))
groom = list(map(str,input()))

len1 = len(bride)
len2 = len(groom)

flag=0
deleteCounter=0
for i in range(0, len1):
    intialLength=len(groom)
    for j in range(0, len2-deleteCounter):
        if bride[i] == groom[j]:
            groom.pop(j)
            flag=1
            deleteCounter+=1
            break
    if(intialLength==len(groom)):
        print(len(bride)-deleteCounter,end='')
        flag=0
        break
if(flag==1):
    print(0,end='')