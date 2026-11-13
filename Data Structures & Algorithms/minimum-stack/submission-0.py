class MinStack:

    def __init__(self):
        self.stack=[] #main stack keeping the actual val
        self.min_stack=[]#twin shadow stack which keeps the minimum val seen at each level

        

    def push(self, val: int) -> None:
        self.stack.append(val)
        cur_min=val if not self.min_stack else min(val,self.min_stack[-1])
        self.min_stack.append(cur_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        
