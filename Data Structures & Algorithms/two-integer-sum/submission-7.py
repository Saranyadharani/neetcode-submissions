class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict={}
        for i,num in enumerate(nums):
            complementary=target-num 
            if complementary in num_dict:
                return [num_dict[complementary],i]
            num_dict[num]=i



































