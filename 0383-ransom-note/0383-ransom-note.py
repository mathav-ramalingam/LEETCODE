class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashy = {}

        for c in magazine:
            hashy[c] = hashy.get(c,0) + 1
        
        for c in ransomNote:
            if c not in hashy or hashy[c] <=0:
                return False
            hashy[c] -= 1
        
        return True