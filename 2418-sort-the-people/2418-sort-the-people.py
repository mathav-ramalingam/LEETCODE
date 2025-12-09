class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        # method 1
        # hashset = list(zip(names,heights))
        # sorted_hashset = sorted(hashset, key = lambda x : x[1], reverse = True)
        # return [name for name,_ in sorted_hashset]

        # method 2:
        return [name for _,name in sorted(zip(heights,names), reverse = True)]