class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        
        if len(s) != len(pattern):
            return False
        else:
            char_to_word = {}
            word_to_char = {}
            is_match = True

            for i in range(len(s)):
                word = s[i]
                char = pattern[i]

                # char to word
                if char in char_to_word:
                    if char_to_word[char] != word:
                        is_match = False
                        break
                else:
                    char_to_word[char] = word

                # word to char
                if word in word_to_char:
                    if word_to_char[word] != char:
                        is_match = False
                        break
                else:
                    word_to_char[word] = char
                            
        return is_match
        
