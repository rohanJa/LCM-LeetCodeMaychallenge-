# Take sum of all array element.
# Make a DP of column being value of array to be included and row being the sum can be made or not
# Then take mid of the sum and make for loop from mid to 0
# min = (sum-diff)//2
# max = min+diff

def calc_min(arr):
    n=len(arr)
    s = sum(arr)
    DP = [[0 for i in range(s+1)] for j in range(n+1)]

    for i in range(n+1):
        DP[i][0] = 1 

    for i in range(1,n+1):
        for j in range(1,s+1):
            DP[i][j]=DP[i-1][j]
            if(arr[i-1]<=j):
                DP[i][j]|=DP[i-1][j-arr[i-1]]

    for i in range(s//2,-1,-1):
        if(DP[n][i]):
            print(i)
            diff=(s-(2*i))
            break
    print(diff)
    return diff


arr = list(map(int,input().split()))
diff = calc_min(arr)
minElement = (sum(arr)-diff)//2
maxElement = minElement+diff
print(maxElement)