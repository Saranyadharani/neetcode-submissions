class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #create a empty stack
        stack=[]
        #loop through each asteriods
        for ast in asteroids:
            #collision only happens when the new ast moves left and top ast moves right
            while stack and ast<0 and stack[-1]>0:
                if stack[-1]<-ast:
                    stack.pop()
                    continue
                elif stack[-1]==-ast:
                    stack.pop()
                ast=0
                break
            if ast!=0:
                stack.append(ast)
        return stack
