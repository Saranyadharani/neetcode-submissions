class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #create a empty stack
        stack=[]
        for token in tokens:
            if token=="+":
                stack.append(stack.pop()+stack.pop())
            elif token=="*":
                stack.append(stack.pop() * stack.pop())
            elif token=="-":
                #order matters
                b=stack.pop()
                a=stack.pop()
                stack.append(a-b)
            elif token=="/":
                #order matters
                b=stack.pop()
                a=stack.pop()
                stack.append(int(a/b))
            else:
                stack.append(int(token))
        return stack[0]