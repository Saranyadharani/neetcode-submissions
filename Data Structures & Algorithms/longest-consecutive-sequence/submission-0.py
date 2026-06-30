class Solution:
    def longestConsecutive(self, nums):
        num_set=set(nums)
        longest=0
        for num in num_set:
            if num-1 not in num_set:
                curr=num
                while curr+1 in num_set:
                    curr+=1
                longest=max(longest,curr-num+1)
        return longest