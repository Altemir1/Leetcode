class Solution(object):
    def sumOfGoodNumbers(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_index = len(nums) - 1
        min_index = 0
        result = 0
        
        def higher_kplus(i):
            if nums[i] > nums[i+k]:
                return True
            return False
        
        def higher_kminus(i):
            if nums[i] > nums[i-k]:
                return True
            return False
        
        for i in range(len(nums)):
            
            if i+k <= max_index and i-k >= min_index: # Both k index exists
                if higher_kminus(i) and higher_kplus(i):
                    result+=nums[i]
            elif i+k <= max_index and i-k < min_index: #Upper boundary exists
                if higher_kplus(i):
                    result+=nums[i]
            elif (i+k) > max_index and (i-k) >= min_index:#Lower boundary exists
                if higher_kminus(i):
                    result+=nums[i]
            else:
                result+=nums[i]
            
        return result
                
                
            