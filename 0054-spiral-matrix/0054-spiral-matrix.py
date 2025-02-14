class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        row_size = len(matrix[0])

        column_size = len(matrix)

        matrix_len = row_size * column_size

        current_direction = 0

        index_list = []

        def final_list(index_list):
            result = []
            for index in index_list:
                x, y = index
                result.append(matrix[x][y])
            return result


        for i in range(row_size):
            index_list.append([0,i])
           
        while len(index_list) != matrix_len:
            x,y = index_list[-1]
            if current_direction == 0: # column-wise pos
                column_size -= 1
                for i in range(column_size):
                    index_list.append([x+1+i, y])

            elif current_direction == 1: # row-wise neg
                row_size -= 1
                for i in range(row_size):
                    index_list.append([x, y-1-i])
            
            elif current_direction == 2: # column-wise neg
                column_size -= 1
                for i in range(column_size):
                    index_list.append([x-1-i, y])
            elif current_direction == 3: # row-wise pos
                row_size -= 1
                for i in range(row_size):
                    index_list.append([x, y+1+i])
                
            current_direction = (current_direction + 1) % 4

        
        return final_list(index_list)

