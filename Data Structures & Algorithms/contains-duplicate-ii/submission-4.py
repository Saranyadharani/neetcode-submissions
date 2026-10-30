class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window=set()
        for i in range(len(nums)):
            if nums[i] in window:
                return True
            window.add(nums[i])
            while len(window)>k:
                window.remove(nums[i-k])
        return False

"""Brute-Force Approach 

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, min(i + k + 1, n)):  # j only needs to go up to i+k
                if nums[i] == nums[j]:
                    return True
        return False

"""
