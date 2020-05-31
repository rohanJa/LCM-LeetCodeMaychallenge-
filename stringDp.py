X = "rohan"
Y = "jainrohan"

arr1=[ [0 for i in range(0,len(X)+1)] for j in range(0,len(Y)+1)]
result1=0
for i in range(1,len(Y)+1):
    for j in range(1,len(X)+1):
        if(Y[i-1]==X[j-1]):
            arr1[i][j]=arr1[i-1][j-1]+1
            result1=max(result1,arr1[i][j])
        else:
            arr1[i][j]=0
print("Result 1 "+str(result1))
arr2=[[0 for i in range(0,len(X)+1)] for j in range(0,len(Y)+1)]
result1=0
for i in range(1,len(Y)+1):
    for j in range(1,len(X)+1):
        if(X[j-1]==Y[i-1]):
            arr2[i][j]=arr2[i-1][j-1]+1
            result1=max(result1,arr2[i][j])
        else:
            arr2[i][j]=max(arr2[i-1][j],arr2[i][j-1])
print("Result 2 "+str(result1))
