t = int(input())

while(t>0):
    n, k = map(int,input().split())
    arr = list(map(int,input().split()))
    ans=''
    for a in arr :

        if(a%k == 0):
            print('1',end='')
            
        else:
            print('0',end='')
    print()
    t-=1