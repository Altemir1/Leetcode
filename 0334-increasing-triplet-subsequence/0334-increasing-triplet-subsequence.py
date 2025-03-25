import sys
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n1, n2 = sys.maxsize, sys.maxsize

        for n in nums:
            if n > n2:
                return True
            if n <= n1:
                n1 = n
            elif n <= n2:
                n2 = n
        
        return False