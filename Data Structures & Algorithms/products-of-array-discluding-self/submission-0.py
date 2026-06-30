class Solution:
    def productExceptSelf(self, nums):
        n=len(nums)
        arr=[1]*n
        left=1
        for i in range(n):
            arr[i]=left
            left*=nums[i]
        right=1
        for i in range(n-1,-1,-1):
            arr[i]*=right
            right*=nums[i]
        return arr
    
        