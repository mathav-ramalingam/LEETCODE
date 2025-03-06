class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:


        # my code testcase fail
        #         s ="acb" t ="ahbgdc"
        #         Output : true
        #         Expected :false

        # count=0
        # s_len = len(s)
        # for char in s:
        #     if char in t:
        #         count=count+1       

        # return count==s_len

        s_len = len(s)
        t_len = len(t)
        i,j = 0,0

        while(i<s_len and j<t_len):
            if s[i] == t[j]:
                i = i+1
                j = j+1
               
            else:
                j = j+1
  
        return i == s_len