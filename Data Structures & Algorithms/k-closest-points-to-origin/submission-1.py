import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #initialize a max heap 
        heap=[]
        # iterate through points and find the dist and add it to the heap
        for x,y in points:
            dist=x*x+y*y
            heapq.heappush(heap,(-dist,x,y))
            if len(heap)>k:
                heapq.heappop(heap)
        return [(x,y) for dist,x,y in heap]
        