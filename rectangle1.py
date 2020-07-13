t = int(input())

'''
                        For x cordinate

As missing points will be in the odd pair xor or of all x cordinate will give the missing x-coordinate 
as x-coordinate will be present who's rectangle points are given.

                        For y cordinate

As missing points will be in the odd pair xor or of all y-coordinate will give the missing y-coordinate 
as x-coordinate will be present who's rectangle points are given.
'''

while(t>0):
    points = int(input())
    x=[]
    y=[]
    missingX = 0
    missingY = 0
    points=4*points-1

    while(points>0):
        l = list(map(int, input().split()))
        x.append(l[0])
        y.append(l[1])
        points-=1

    for xCord in x:
        missingX^=xCord
    for yCord in y:
        missingY^=yCord
    print(str(missingX)+' '+str(missingY))

    t-=1