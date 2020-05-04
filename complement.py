class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        res = ''
        while num > 0:
            lsb = num & 1
            if lsb == 1:
                res = '0' + res #In this we havent use res+='0' or '1' beacuse it is done to maintain order of the complement of the corresponding number
            else:
                res = '1' + res
            num = num >> 1
        return int(res,2)
    