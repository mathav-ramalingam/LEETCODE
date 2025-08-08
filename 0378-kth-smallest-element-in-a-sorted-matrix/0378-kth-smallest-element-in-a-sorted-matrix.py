class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        singleList = []
        for row in matrix:
            singleList = singleList + row

        singleList.sort()

        return singleList[k - 1]
