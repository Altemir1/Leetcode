class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if len(flowerbed) == 1 and n == 1:
            if flowerbed[0] == 0:
                return True
            else:
                return False

        if n == 0:
            return True 

        
        for i in range(len(flowerbed)):
            if i == 0:
                if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    n -= 1
                    flowerbed[i] = 1
            elif i == len(flowerbed) - 1:
                if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                    n -= 1
                    flowerbed[i] =1
            else:
                if flowerbed[i] == 0 and flowerbed[i-1]==0 and flowerbed[i+1] ==0:
                    n -= 1
                    flowerbed[i] = 1
            
        if n <= 0:
            return True
        else:
            return False