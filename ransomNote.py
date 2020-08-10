class Solution(object):
    def canConstruct(self, ransomNote, magazine):

        ransomCount={}
        magazineCount={}
        
        for ch in ransomNote:
            if ch in ransomCount:
                ransomCount[ch]+=1
            else:
                ransomCount[ch]=1    
                
        for ch in magazine:
            if ch in magazineCount:
                magazineCount[ch]+=1
            else:
                magazineCount[ch]=1
        
        for ch in ransomNote:
            if ch in magazine:
                if ransomCount[ch] > magazineCount[ch]:
                    return False
            else:
                return False
                
        return True    




arr = list(map(int,input().split()))

count = [1 for val in arr ]

for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[j]<arr[j])