class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        
        sentence =''
        word_count = 0
        for c in word:
            sentence = sentence + c
            if c == ch and word_count == 0:
                sentence = sentence[::-1]
                word_count += 1
                
        return sentence

