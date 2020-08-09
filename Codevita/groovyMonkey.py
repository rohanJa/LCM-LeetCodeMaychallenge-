pos = list(map(int,input().split()))
flag=0
arr = [i+1 for i in range(len(pos))]
temp=[i+1 for i in range(len(pos))]
counter=0
while(True):
    sortedCheck = 0
    counter+=1
    for index in range(len(pos)):
        temp[pos[index]-1]=arr[index]
    arr=temp.copy()   
    print("\t" +str(arr))    
    for i in range(len(pos)):
        if(i+1!=arr[i]):
            break 
        sortedCheck+=1
    if(sortedCheck==len(pos)):
        print(counter)
        break