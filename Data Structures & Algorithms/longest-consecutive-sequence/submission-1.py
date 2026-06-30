class Solution:
    def longestConsecutive(self, nums):
       nums_set=set(nums)
       longest=0
       for num in nums_set:
        if num-1 not in nums_set:
            curr=num
            while curr+1 in nums_set:
                curr+=1
            longest=max(longest,curr-num+1)
       return longest