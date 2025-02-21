class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result = []
        flag = False
        for i in range(len(candies)):
            for j in range(len(candies)):
                if candies[i] + extraCandies < candies[j]:
                    flag = False
                    break
                else:
                    flag = True
            result.append(flag)

        return result