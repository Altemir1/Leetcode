class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        lem_price = 5
        change = [0, 0, 0]

        for bill in bills:
            if bill == 5:
                change[0] += 1
            elif bill == 10:
                if change[0] >= 1:
                    change[0] -= 1
                    change[1] += 1
                else:
                    return False
            else:
                if change[0] >= 1 and change[1] >= 1:
                    change[2]+=1
                    change[1]-=1
                    change[0]-=1
                elif change[0] >= 3:
                    change[2]+=1
                    change[0]-=3
                else: 
                    return False
        
        return True
