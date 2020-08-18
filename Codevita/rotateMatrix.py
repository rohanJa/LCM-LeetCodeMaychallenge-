m, n = map(int,input().split())

mat=[]
def rotateMatrix(mat,row): 
  
    if not len(mat): 
        return
      
    for sh in range(0,len(row)):
        if((sh)%2==1):
            # print('odd and anticlockwise ')
            for val in range(0,row[sh]): 

                top = sh-1
                bottom = len(mat)-1-sh
            
                left = sh
                right = len(mat[0])-1-sh
            
                # while left < right and top < bottom: 
            
                # Store the first element of next row, 
                # this element will replace first element of 
                # current row 
                prev = mat[top+1][left] 

                # Move elements of top row one step right 
                for i in range(left, right+1): 
                    curr = mat[top][i] 
                    mat[top][i] = prev 
                    prev = curr 

                top += 1

                # Move elements of rightmost column one step downwards 
                for i in range(top, bottom+1): 
                    curr = mat[i][right] 
                    mat[i][right] = prev 
                    prev = curr 

                right -= 1

                # Move elements of bottom row one step left 
                for i in range(right, left-1, -1): 
                    curr = mat[bottom][i] 
                    mat[bottom][i] = prev 
                    prev = curr 

                bottom -= 1

                # Move elements of leftmost column one step upwards 
                for i in range(bottom, top-1, -1): 
                    curr = mat[i][left] 
                    mat[i][left] = prev 
                    prev = curr 

                left += 1
        else:
            # print('even and clockwise ')
            for val in range(0,row[sh]): 
                # print("Value of val "+str(val))
                top = sh
                bottom = len(mat)-(1)-sh
            
                left = sh
                right = len(mat[0])-(1)-sh
                
                # Store the first element of current row, 
                # this element will replace second element of 
                # current column 
                prev = mat[top+1][right] 
                
                
                # Move elements of top row one step left 
                for i in range(right,left-1,-1 ): 
                    curr = mat[top][i] 
                    mat[top][i] = prev 
                    prev = curr 
                
                # Move elements of leftmost column one step upwards 
                for i in range(top+1,bottom+1): 
                    curr = mat[i][left] 
                    mat[i][left] = prev 
                    prev = curr 

                # Move elements of bottom row one step right 
                
                for i in range(left+1,right+1): 
                    curr = mat[bottom][i] 
                    mat[bottom][i] = prev 
                    prev = curr 

                # Move elements of rightmost column one step upwards 
                for i in range(bottom,top,-1): 

                    curr = mat[i-1][right] 
                    mat[i-1][right] = prev 
                    prev = curr
    return mat 
    
for i in range(0,n):
    mat.append(list(map(int,input().split())))

# take input to which row to rotate
# print("Input rotation list")

r=list(map(int,input().split()))


# Taking input of the matrix rotation list

rotateMatrix(mat,r)
# print("Ouput is ")
for i in range(0,n):
    for j in range(0,m):
        print(mat[i][j],end=' ')
    print()
print()