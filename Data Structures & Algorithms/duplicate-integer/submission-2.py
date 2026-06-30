class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        left=0
        window=set()
        for right in range(len(nums)):
            if nums[right] in window:
                return True
            window.add(nums[right])
        return False