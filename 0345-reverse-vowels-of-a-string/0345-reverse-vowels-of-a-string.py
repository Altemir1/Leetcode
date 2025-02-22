class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel_list = ["a", "e", "i", "o", "u"]
        s = list(s)
        vowel_index = []
        vowels = []
        
        for i in range(len(s)):
            if s[i].lower() in vowel_list:
                vowel_index.append(i)
                vowels.append(s[i])
        
        vowel_index_reversed = vowel_index[::-1]
        
        for i in range(len(vowels)):
            s[vowel_index_reversed[i]] = vowels[i]
        
        return "".join(s)

        
            

            
        
        