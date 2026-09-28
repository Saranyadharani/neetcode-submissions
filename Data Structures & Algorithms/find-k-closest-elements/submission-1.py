import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap=[] #use max heap
        for num in arr:
            dist=abs(num-x)
            heapq.heappush(heap,(-dist,-num))
            if len(heap)>k:
                heapq.heappop(heap)
        result=[-num for dist,num in heap]
        return sorted(result)