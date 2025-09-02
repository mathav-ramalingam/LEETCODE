# My apprach time limit exceed 
    # strs = ["a","bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"]

# from itertools import permutations

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         res = []

#         while strs:
#             stack = []
#             word = strs.pop(0)
#             stack.append(word)

#             perm = {"".join(p) for p in permutations(word)}
#             # print(perm)
            
#             remaining = []
#             for w in strs:
#                 if w in perm:
#                     stack.append(w)
#                 else:
#                     remaining.append(w)
            
#             strs = remaining
#             res.append(stack)

#         return res


from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
           key = "".join(sorted(word))
           anagrams[key].append(word)

        return list(anagrams.values())