class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]: 
        l = len(matrix)
        top,left = 0,0
        down, right = len(matrix) - 1, len(matrix[0]) - 1 
        
        res =[]
        while top <= down and left <= right:

            for i in range(left,right+1):
                res.append(matrix[top][i])
            top = top+1

            for i in range(top , down+1):
                res.append(matrix[i][right])
            right = right-1
            
            if top <= down:
                for i in range(right, left - 1, -1):
                    res.append(matrix[down][i])
                down -= 1
                
            if left <= right:
                for i in range(down, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res
        