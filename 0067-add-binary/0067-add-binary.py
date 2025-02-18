class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
       
      
        if len(a) >= len(b):
            bigger_element = list(a)  
            smaller_element = b
        else:
            bigger_element = list(b)
            smaller_element = a

        carry = 0
        smaller_len = len(smaller_element)
        bigger_len = len(bigger_element)

       
        for i in range(1, smaller_len + 1):
            sum_value = carry + int(bigger_element[-i]) + int(smaller_element[-i])
            
            bigger_element[-i] = str(sum_value % 2)
            carry = sum_value // 2

       
        for i in range(smaller_len + 1, bigger_len + 1):
            if carry == 0:
                break  

            sum_value = carry + int(bigger_element[-i])
            bigger_element[-i] = str(sum_value % 2)
            carry = sum_value // 2

        
        if carry:
            bigger_element.insert(0, "1")

        return "".join(bigger_element)