class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #setting the minspeed and maxspeed
        left=1
        right=max(piles)
        result=right
        while left<=right:
            mid=(left+right)//2
            hour=0
            for p in piles :
                hour+=(p+mid-1)//mid
            if hour<=h:
                result=mid
                right=mid-1
            else:
                left=mid+1
        return result