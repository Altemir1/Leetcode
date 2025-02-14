class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        def find_zeros():
            zero_index = []
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    if matrix[i][j] == 0:
                        zero_index.append([i, j])
            return zero_index
        
        def change_row(matrix, x):
            for i in range(len(matrix[x])):
                matrix[x][i] = 0
        
        def change_column(matrix, y):
            for i in range(len(matrix)):
                matrix[i][y] = 0

        
        zero_index = find_zeros()

        for index in zero_index:
            x, y = index
            change_row(matrix, x)
            change_column(matrix, y)
        
        return matrix

