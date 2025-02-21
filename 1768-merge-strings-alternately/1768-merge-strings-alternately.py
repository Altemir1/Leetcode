class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = ""
        length1 = len(word1)
        length2= len(word2)
        for i in range(max(length1, length2)):
            if i < length1:
                result += word1[i]
            if i < length2:
                result += word2[i]
        
        return result

            
        