class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hashset = list(zip(names,heights))
        sorted_hashset = sorted(hashset, key = lambda x : x[1], reverse = True)
        return [name for name,_ in sorted_hashset]
