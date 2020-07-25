t = int(input())
while(t>0):
    s = int(input())
    arr = list(map(int,input().split()))
    a = min(arr)
    b = max(arr)

    tempA = str(bin(a))[2:] 
    tempB = str(bin(b))[2:]
    aB = tempA + tempB 
    bA = tempB + tempA
    # print(aB)
    # print(bA)
    print(int(aB,2) - int(bA,2))
    t-=1