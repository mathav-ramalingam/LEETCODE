class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        target_idx = 0
        i = 1
        while(i<=n and target_idx != len(target)):
            if i == target[target_idx]:
                stack.append("Push")
                target_idx += 1
            else:
                stack.append("Push")
                stack.append("Pop")
            i += 1

        return stack
        