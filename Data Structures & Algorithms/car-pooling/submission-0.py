import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        if not trips:
            return True
        # sort the trips based on the pickup location
        trips.sort(key=lambda x:x[1])
        #create a min heap based on the drop location and assign a var for calculation the passengers
        heap=[]
        current=0
        for num,frm,to in trips:
            while heap and heap[0][0]<=frm:
                _,n=heapq.heappop(heap)
                current-=n
            current+=num
            if current>capacity:
                return False
            heapq.heappush(heap,(to,num))
        return True
