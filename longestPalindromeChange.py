s='0011'
k=1

result = [0 for val in s]
mark = [0 for val in s]

l=0
r=len(s)-1

while(l<=r):
    if(l==r):
        result[l]=s[l]
        break

    if(s[l]==s[r]):
        result[l]=s[l]
        result[r]=s[r]
    else:    
        if(s[l]>=s[r]):
            result[l]=s[l]
            result[r]=s[l]
            k=k-1
            mark[r]=1

        else:
            result[l]=s[r]
            result[r]=s[r]
            mark[l]=1
            k=k-1

    l=l+1
    r=r-1

if(k<0):
    print("-1\n")

l=0
r=len(s)-1

while(l<=r):
    if(l==r):
        if(result[l]<'9' and k>=1):
            result[l]='9'
        break

    if(result[l]<'9'):
        if((mark[l]==1 or mark[r]==1 ) and k>=1):
            result[l] = '9'
            result[r] = '9'
            k=k-1
        elif((mark[l]==0 and mark[r]==0 ) and k>=2):
            result[l] = '9'
            result[r] = '9'
            k=k-2
        
    l=l+1
    r=r-1

print(result)
'''
if(l==r):
    result[l]=s[l]

if(l==r):
    if(result[l]<9 and k>=1):
        result[l]=9
    break
'''