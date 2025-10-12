# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         max_len = 0
#         i =0 

#         while i < len(s):
#             j = i

#             while j < len(s):
#                 sub_str = s[i:j+1]

#                 if len(sub_str) == len(set(sub_str)):
#                     max_len = len(sub_str) if len(sub_str) > max_len else max_len
#                 else:
#                     break
                
#                 j += 1
#             i += 1
    
#         return max_len



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_str = []
        max_len = 0

        for ch in s:
            if ch in sub_str:
                idx = sub_str.index(ch)
                sub_str = sub_str[idx+1:]
                # print(sub_str)
            sub_str.append(ch)
            max_len = max(max_len,len(sub_str))

        
        return max_len

        

        