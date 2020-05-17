for x in range((int(input()))):
    n,k=map(int,input().split())
    list_=list(map(int,input().split()))
    count=0
    if(k in list_):
        for j in range(len(list_)-k+1):
            check=0
            if(list_[j]==k):
                for i in range(j,j+k-1):
                    if(list_[i]==list_[i+1]+1):
                        check+=1
                    else:
                        break
                if(check==k-1):
                    count+=1
    print("Case #"+str(x+1)+":",count)