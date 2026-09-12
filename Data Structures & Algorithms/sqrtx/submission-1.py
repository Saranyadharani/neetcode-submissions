class Solution:
    def mySqrt(self, x: int) -> int:
        #setting the search space between 0 and x 
        left=1
        right=x
        result=0
        while left<=right:
            mid=(left+right)//2
            if mid*mid<=x:
                result=mid #store the result to the mid
                left=mid+1 #try for better answer
            else:
                right=mid-1
        return result