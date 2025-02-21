class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        tail = len(str2)
        common_divisor = ""
        while tail >= 2:
            common_divisor = str2[:tail]
            if len(str1) % len(common_divisor) == 0:
                quan_sub_1 = len(str1) / len(common_divisor)
                quan_sub_2 = len(str2) / len(common_divisor)
                if str1 == quan_sub_1 * common_divisor and str2 == quan_sub_2 * common_divisor:
                    return common_divisor
                else:
                    tail -=1
            else:
                tail-=1
        
        return ""