
a="polikujmnhytgbyfredcxswqaz"
b="qwryupcsfoghjkldezxvbintma"

in_ = 'aab'

print(in_.replace('a','',1)) 

str_=""
pos=27
in1_=in_
for val in in1_:
    pos=27
    for temp in in_:
        if pos >a.index(temp):
            pos=a.index(temp)
    str_+=a[pos]
    in_=in_.replace(a[pos],'',1) # to remove one occurence of the character in the string
    
print(str_)