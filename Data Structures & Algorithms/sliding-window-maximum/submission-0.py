from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # define the result list and deque
        result=[]
        dq=deque()
        for i in range(len(nums)):
            # popout the elements that falls outside the window
            while dq and dq[0]<i-k+1: 
                dq.popleft()
            #popout the back elements smaller than the current window element values
            while dq and nums[dq[-1]]<=nums[i]: 
                dq.pop()
            #else store the current index to the queue
            dq.append(i)
            if i>=k-1: # record the max value in the current window
                result.append(nums[dq[0]])
        return result 