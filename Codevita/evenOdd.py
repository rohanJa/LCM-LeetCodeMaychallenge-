low,high = map(int,input().split())

k = int(input())

lst=[]
e=[]
o=[]

for i in range(low,high+1):
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
el=len(e)
ol=len(o)

res=0.5*((ol+el)**k +(el-ol)**k)
print(int(res))