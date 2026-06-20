class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        top=-1
        op=['+','-','/','*']
        stack=[]
        for i in tokens:
            if i not in op:
                top+=1
                stack.append(int(i))
            if i in op:
                op2=stack[top] #else op2=stack.pop()
                op1=stack[top-1] #else op1=stack.pop()
                if i == "+":
                    value = op1 + op2
                elif i == "-":
                    value = op1 - op2
                elif i == "*":
                    value = op1 * op2
                elif i == "/":
                    value = int(op1 / op2)
                stack.pop()
                stack.pop()
                top-=2
                stack.append(value)
                top+=1
        return stack[top]
        
