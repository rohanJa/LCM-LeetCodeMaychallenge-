# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        first=1
        last=n
        result=-1
        while( first<=last):
            mid = (first + (last-first)//2)
            if(isBadVersion(mid)):
                last = mid - 1
                result=mid
            else:
                first=mid+1
                
        return result