import math

try:
    print(1/0)
except:
    print("infinity")
    
print(math.gcd(2,4 ))
print(math.floor(3.4))
print(abs(-9))
print(int(math.sqrt(4)))
print(int('111',2))
print(str(bin(10))[2:])

s="aAfaf"

print(s.index('a'))
print(math.gcd(111111111111111,1111111111111111))

print(' 2 1')
print((' 2 '.strip()))
print(str(bin(2))[::-1])
print(int('1111',2))
a=[3,12,5,53,4]
a.sort()
print(a)

f={
    1:"asas",
    2:"3",
    3:3
}
l=list(f)
print(l)
v=list(f.values()) #dict values stored in form of list
print(v)
k=list(f.keys()) #dict keys stored in form of list
print(k)

s="print rohan"
print(s.replace("p","")) #it doesnot replace the char permanentaly we have ot store it
print(s) # p is not removed from the string

s=s.replace("p","")

print(s) # s is now removed

n = list(map(int,input().split()))

#rotation
a=1
print(str[-a:]+str[:-a])

#reverse
print(str[-1::-1])


#upper and lower method change temperoraliy in string we have to save it in a variable
#upper and lower case 

s="print rAsf"
print(s.upper())
print(s.lower())
print(s.islower())
print(s.islower())

a="alsfmkasas"
b="assfl13"
c='13225'
# isalnum will print True both for pure string (containing character) and string containing numeric
print(b.isalpha())#if string only contain alphabet
print(a.isalnum())#if string has all alphanumericc character
print(c.isnumeric()) #only contain int in the string

