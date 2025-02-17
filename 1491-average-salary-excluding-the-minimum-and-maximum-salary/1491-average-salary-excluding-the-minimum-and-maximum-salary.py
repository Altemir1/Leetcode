from decimal import Decimal
class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        result = (Decimal(sum(salary)) - Decimal(max(salary)) - Decimal(min(salary))) / Decimal(len(salary) - 2)
        return float(result.quantize(Decimal("0.00001")))  # Ensures 5 decimal places


