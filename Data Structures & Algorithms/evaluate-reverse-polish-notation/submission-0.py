class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numstack = []
        opers = ["+", "-", "*", "/"]
        for token in tokens:
            if token in opers:
                num2 = int(numstack.pop())
                num1 = int(numstack.pop())
                numstack.append(self.calculate(num1, num2, token))
            else:
                numstack.append(token)
        return numstack[0]

    def calculate(self, num1, num2, oper) -> int:
        if oper == "+":
            return num1 + num2
        elif oper == "-":
            return num1 - num2
        elif oper == "/":
            return num1 // num2
        elif oper == "*":
            return num1 * num2
        else:
            return null