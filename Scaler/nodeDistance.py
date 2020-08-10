node = int(input())

B = [
    [1,2,11],
    [1,3,5],
    [2,4,3],
    [2,5,14]
]

freq = {}

for i in range(len(B)):
    if B[0] in freq:
        freq[B[0]]+=1
    else:
        freq[B[0]]=1

