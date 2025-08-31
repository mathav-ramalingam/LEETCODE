class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        else:
            s_to_t = {}
            t_to_s = {}
            is_match = True

            for i in range(len(s)):
                ch1 = s[i]
                ch2 = t[i]

                if ch1 in s_to_t:
                    if s_to_t[ch1] != ch2:
                        is_match = False
                        break
                else:
                    s_to_t[ch1] = ch2

                if ch2 in t_to_s:
                    if t_to_s[ch2] != ch1:
                        is_match = False
                        break
                else:
                    t_to_s[ch2] =ch1
        
        return is_match