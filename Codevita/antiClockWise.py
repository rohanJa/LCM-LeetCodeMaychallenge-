m, n = map(int,input().split())

mat=[]
def rotateMatrix(mat): 
  
    if not len(mat): 
        return
      
    """ 
        top : starting row index 
        bottom : ending row index 
        left : starting column index 
        right : ending column index 
    """
  
    top = 0
    bottom = len(mat)-1
  
    left = 0
    right = len(mat[0])-1    
    
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
    
for i in range(0,m):
    mat.append(list(map(int,input().split())))


# Taking input of the matrix rotation list
rotateMatrix(mat)
rotateMatrix(mat)

print("Ouput is ")
for i in range(0,m):
    for j in range(0,n):
        print(mat[i][j],end=' ')
    print()