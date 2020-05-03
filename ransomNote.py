class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
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