class Solution:
    def calculate(self, s: str) -> int:

        def precition(op):
            if op in ("+","-"):
                return 1
            elif op in ("*","/"):
                return 2
            elif op in ("^"):
                return 3
            return 0

        def calculate(a, b, op):
            if op == "+": return a+b
            elif op == "-": return a-b
            elif op == "*": return a*b
            elif op == "/": return a//b
            elif op == "^": return a**b
        

        num_stack = deque()
        op_stack = deque()

        n = len(s)
        i =0

        while i < n:
            if s[i] == " ":
                i += 1
                continue
            elif s[i].isdigit():
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                num_stack.append(num)
                continue
            else:
                while op_stack and precition(op_stack[-1]) >=  precition(s[i]):
                    b = num_stack.pop()
                    a = num_stack.pop()
                    num_stack.append(calculate(a, b, op_stack.pop()))
                op_stack.append(s[i])
            i+= 1
        
        while op_stack:
            b = num_stack.pop()
            a = num_stack.pop()
            num_stack.append(calculate(a, b, op_stack.pop()))
        
        return num_stack[-1]
        
            