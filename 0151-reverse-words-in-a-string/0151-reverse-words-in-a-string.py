class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        s = s.strip()
        s = s.split(" ")

        for element in s:
            if len(element) != 0:
                result.append(element)
               
            
            
        return " ".join(result[::-1])
