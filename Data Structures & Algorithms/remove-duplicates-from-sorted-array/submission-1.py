class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # use fast and slow pointer
        slow=1
        for fast in range(len(nums)):
            if nums[fast]!=nums[slow-1]:
                nums[slow]=nums[fast]
                slow+=1
        return slow














"""Brute Force approach

        1. using sorting and set
        return sorted(set(nums))

        2. using a new list
        unique=[]
        for x in nums:
            if not unique or unique[-1]!=x:
                unique.append(x)
        nums[:len(unique)]=unique
        return len(unique)

        """