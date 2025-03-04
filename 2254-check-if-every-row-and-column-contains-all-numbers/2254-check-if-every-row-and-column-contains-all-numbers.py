class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:

        # my code 
        # n = len(matrix)
        # test = set()
        # for i in range(1,n+1):
        #     test.add(i)

        # for i in range(0,n):
        #     for j in range(1,n):
        #         if matrix[i][j] == matrix[i][j-1]:
        #             return False

        #         if matrix[i][j] not in test:
        #             return False

        # return True
                
        n = len(matrix)
        test_set = set(range(1,n+1))

        for i in range(n):
            if set(matrix[i]) != test_set or set(row[i] for row in matrix) != test_set:
                return False

        return True


        