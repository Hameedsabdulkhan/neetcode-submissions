class Solution(object):
    def evalRPN(self, tokens):
        stack=[]
        x=0
        for i in tokens:
            if(i=='+'):
                x=stack[-1]+stack[-2]
                stack.pop()
                stack.pop()
                stack.append(x)
            elif(i=='*'):
                x=stack[-1]*stack[-2]
                stack.pop()
                stack.pop()
                stack.append(x)
            elif(i=='-'):
                x=stack[-2]-stack[-1]
                stack.pop()
                stack.pop()
                stack.append(x)
            elif(i=='/'):
                x=int(stack[-2] / stack[-1])
                stack.pop()
                stack.pop()
                stack.append(x)
            else:
                stack.append(int(i))
        return stack[0]    