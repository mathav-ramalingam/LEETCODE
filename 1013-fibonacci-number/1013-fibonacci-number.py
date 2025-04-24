class Solution:
    def fib(self, n: int) -> int:
        seq = [0,1]
        for i in range(n):
            seq.append(seq[-1] + seq[-2])

        return seq[-2]
        