from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # method 1
        # return Counter(s) == Counter(t)

        # method 2
        s = sorted(s)
        t = sorted(t)
        return s == t