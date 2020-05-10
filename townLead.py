class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        
        a=[0]*(N+1)
        b=[0]*(N+1)
        
        for val in trust:
            a[val[0]]+=1
            b[val[1]]+=1
            
        for i in range(1,N+1):
            if( b[i]==N-1 and a[i]==0):
                return i
        
        return -1
