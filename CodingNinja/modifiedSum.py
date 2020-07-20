t = int(input())
# def sos():

while(t>0):
    size, multi = list(map(int,input().split()))

    arr = list(map(int,input().split()))
    sum=0
    if(multi==0):
        for i in range(0,n):
            if(arr[i]>0):

    if(multi<0)
        max_so_far = 0 
        curr_max = 0 
        for i in range(0,size): 
            if(arr[i]<0):
                curr_max = max(a[i], curr_max + a[i]) 
                max_so_far = max(max_so_far,curr_max) 
        
    t-=1