class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens)< 2:
            return int(tokens[0])
        stack = []
        for i in range(len(tokens)):
            if tokens[i].isdigit() or (tokens[i].startswith('-') and tokens[i][1:].isdigit()):
                stack.append(tokens[i])
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if tokens[i] == "+":
                    stack.append(num1+num2)
                elif tokens[i] == "-":
                    stack.append(num1 - num2)
                elif tokens[i] == "*":
                    stack.append(num1 * num2)
                elif tokens[i] == "/":
                    stack.append(int(num1 / num2))
        return stack.pop()

