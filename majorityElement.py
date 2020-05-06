class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict_={}
        for val in nums:
            if val in dict_:
                dict_[val]+=1
            else:
                dict_[val]=1
        
        for val in dict_:
            if dict_[val]>len(nums)//2:
                return val