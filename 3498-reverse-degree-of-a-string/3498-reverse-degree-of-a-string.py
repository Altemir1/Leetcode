class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        letter_degree = {}
        count = 26
        for i in range(97, 123):
            letter_degree[chr(i)] = count
            count-= 1
        
        result = 0
        for i in range(len(s)):
            multiplier = i + 1
            result += multiplier * letter_degree[s[i]]
        
        return result