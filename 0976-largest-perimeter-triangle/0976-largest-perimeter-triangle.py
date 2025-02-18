class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def quicksort(nums):
            if len(nums) <= 1:
                return nums  

            pivot = nums[len(nums) // 2]  
            left = [x for x in nums if x > pivot]  
            middle = [x for x in nums if x == pivot] 
            right = [x for x in nums if x < pivot] 

            return quicksort(left) + middle + quicksort(right)
        
        nums = quicksort(nums)

        for i in range(len(nums) - 2):
            if  nums[i] + nums[i+1] > nums[i+2] and nums[i] < nums[i+1] + nums[i+2] and nums[i] + nums[i+2] > nums[i+1]:
                return nums[i] + nums[i+1] + nums[i+2]
            
        return 0


            

            