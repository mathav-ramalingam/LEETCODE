class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        # # my approach : number = "133235"
        #                 digit = "3"
        #         Use Testcase : Output = "13235"
        #                         Expected = "13325"

        # num = [int(char) for char in number]
        # digit = int(digit)
        # if digit in num:
        #     num.remove(digit)
        
        # return "".join(map(str,num))

        maxi = float('-inf')
        for i in range(len(number)):
            if number[i] == digit:
                x = number[0:i] + number[i+1 :]
                maxi = max(maxi,int(x))
        
        return str(maxi)