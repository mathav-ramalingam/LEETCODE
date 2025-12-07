class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:

        def up(s):
            return [ch for ch in s if ch.isupper()]

        def isSubquence(pattern,q):
            iters = iter(q)
            return all(ch in iters for ch in pattern)

        return [up(pattern) == up(q) and isSubquence(pattern,q) for q in queries]


