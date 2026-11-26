class Solution:
    def canAliceWin(self, n: int) -> bool:

        def play(stones, remove):
            if stones < remove:
                return False
                
            return not play(stones - remove, remove - 1)

        return play(n, 10)