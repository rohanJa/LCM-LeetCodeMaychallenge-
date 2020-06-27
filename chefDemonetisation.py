t = int(input())

while t>0 :
    s,n = map(int, input().split(' '))
    count=0
    count+=s//n
    
    rem=s%n
    if(s%n==1):
        count+=1
    elif(rem%2!=0 and s%n!=0):
        count+=2
    if(rem!=0 and rem%2==0):
        count+=1
    
    print(count)
    t-=1