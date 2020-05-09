class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        i=1
        
        while(i*i<=num):
            if(num%i==0 and num/i==i):
                return True
            i+=1
        return False
        