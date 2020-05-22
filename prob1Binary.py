# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

list_=[1,2,3,4,5,6,19,21]
high=len(list_)
low=0
n=5

while(low<=high):
    print("iteration ")
    mid=high+(low-high)//2
    if(list_[mid]==n):
        print("Number found "+str(list_[mid]))
    if(list_[mid]<n):
        low=mid+1
    else:
        high=mid-1