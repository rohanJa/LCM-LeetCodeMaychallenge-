n=int(input())
l=0
while(n!=0):
    a=n%10
    l*=10+a
    n//=10
    print(l)
    print(a)
if(l==n):
    print("Its an palindrome")
else:
    print("Its not an palindrome")