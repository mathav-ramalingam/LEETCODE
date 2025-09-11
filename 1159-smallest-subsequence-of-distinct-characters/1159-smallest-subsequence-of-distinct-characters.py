class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        occurence = {letter:idx for idx, letter in enumerate(s)}
        seen = set()

        for idx , letter in enumerate(s):
            if letter not in seen:
                while stack and stack[-1] > letter and occurence[stack[-1]] > idx:
                    seen.remove(stack.pop())

                seen.add(letter)
                stack.append(letter)

        return "".join(stack)
