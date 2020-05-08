class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        
        if(len(coordinates)<=2):
            return True
        try:
            val1 = (coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0])
        except ZeroDivisionError:
            val1=-1
            
        for val in range(1,len(coordinates)-1):
            try:
                m = (coordinates[val+1][1]-coordinates[val][1])/(coordinates[val+1][0]-coordinates[val][0])
            except ZeroDivisionError:
                m=-1
            if m!= val1:
                return False
                
        return True
        