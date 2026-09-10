import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # using hashmap to get the freq of the elements in nums
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        # initialize a heap
        heap=[]
        # iterate through hashmap
        for num,count in freq.items():
            heapq.heappush(heap,(count,num))
            if len(heap)>k:
                heapq.heappop(heap)
        return [num for count,num in heap]