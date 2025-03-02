class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        top = 0
        down = n-1
        left =0 
        right = n-1
        num=1

        while left <= right and top<= down:

            for i in range(left,right+1):
                matrix[top][i] = num
                num = num+1
            top = top+1

            for i in range(top , down+1):
                matrix[i][right] =  num
                num = num+1
            right = right -1

            if top <= down:
                for i in range(right, left - 1, -1):
                    matrix[down][i] = num
                    num += 1
                down -= 1

            if left <= right:
                for i in range(down, top - 1, -1):
                    matrix[i][left] = num
                    num += 1
                left += 1
  
        return matrix




        # while left <= right and top<= down:
        #     for i in range(left,right+1):
        #         matrix[top][i] = num
        #         num = num+1
        #     top = top+1
        #     for i in range(top , down+1):
        #         matrix[i][right] =  num
        #         num = num+1
        #     right = right -1

        #     for i in range(right, left - 1, -1):
        #         matrix[down][i] = num
        #         num += 1
        #     down -= 1

        #     for i in range(down, top - 1, -1):
        #         matrix[i][left] = num
        #         num += 1
        #     left += 1
  
        # return matrix

        