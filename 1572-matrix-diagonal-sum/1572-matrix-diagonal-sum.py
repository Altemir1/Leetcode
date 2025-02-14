class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        result = 0
        
        
        for i in range(len(mat)):
            left_i = 0 + i
            right_i = -1 - i
            if left_i == right_i + len(mat):
                result += mat[i][left_i] 
            else:
                result += mat[i][left_i]
                result += mat[i][right_i]
        
        return result




        