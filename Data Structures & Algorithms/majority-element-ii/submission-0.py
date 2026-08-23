class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        map={}
        result=[]
        n=len(nums)
        for num in nums:
            map[num]=map.get(num,0)+1
        for num,count in map.items():
            if count>n//3:
                result.append(num)
        return result