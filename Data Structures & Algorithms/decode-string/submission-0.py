class Solution:
    def decodeString(self, s: str) -> str:
        #create a empty stack
        stack=[]
        #loop through each char in string 
        for char in s:
            if char!="]":
                stack.append(char)
            else:
                substr=""
                while stack and stack[-1]!="[":
                    substr=stack.pop()+substr
                stack.pop()
                k=""
                while stack and stack[-1].isdigit():
                    k=stack.pop()+k
                stack.append(int(k)*substr)
        return "".join(stack)