ar=list(map(int,input().split(' ')))

sum1=0
mod=1000000000+7

'''
for i in range(0,len(ar)-1):
    for j in range(i+1,len(ar)):
        sum1=sum1%mod+(ar[i]^ar[j])%mod
    sum1 = sum1%mod
'''

for index,a in enumerate(ar):
    print("index "+str(index)+" a "+str(a)+" last "+str(a|0))
print((2*sum1)%mod)