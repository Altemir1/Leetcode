class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if len(coordinates) < 3:
            return True  

        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        for i in range(2, len(coordinates)): 
            x3, y3 = coordinates[i]

            cross_product = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

            if cross_product != 0:  
                return False

        return True
            

        

       
