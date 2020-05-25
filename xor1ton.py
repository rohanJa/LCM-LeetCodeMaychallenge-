def xor(n):
    if(n%4==0):
        return n
    elif(n%4==1):
        return 1
    elif(n%4==2):
        return n+1
    elif(n%4==3):
        return 0

if __name__ =="__main__":
    n=int(input())
    print(xor(n))
