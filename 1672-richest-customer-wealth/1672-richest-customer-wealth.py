class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_money = 0
        
        for account in accounts:
            total_money = 0
            for money in account:
                total_money += money
                if max_money <= total_money:
                    max_money = total_money


        return max_money
                

