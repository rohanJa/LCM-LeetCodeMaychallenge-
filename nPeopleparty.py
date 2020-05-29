# hackwithinfy 2019 2 round question 

n =list(map(int,input().split()))
print(n)
people=int(input())
previous_sum=sum(n)
while people>0:
    l=list(map(int,input().split()))
    current_sum=sum(l)
    print(previous_sum-current_sum)
    previous_sum=current_sum
    people=people-1