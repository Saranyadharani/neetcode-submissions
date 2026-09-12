class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # define the smaller and larger capacity 
        left=max(weights)#minimum capacity
        right=sum(weights)#maximum capacity
        result=right#initiaize result as right
        while left<=right:
            mid=(left+right)//2
            days_needed=1
            current_load=0
            for w in weights:
                if current_load+w>mid:
                    days_needed+=1
                    current_load=0
                current_load+=w
            if days_needed<=days:
                result=mid
                right=mid-1
            else:
                left=mid+1
        return result