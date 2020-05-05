class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        li={}
        for val in s:
            if val not in li:
                li[val]=1
            else:
                li[val]+=1
        print(li)
        val=-1
        for val in s:
            if(li[val]==1):
                return s.index(val)
        return -1    