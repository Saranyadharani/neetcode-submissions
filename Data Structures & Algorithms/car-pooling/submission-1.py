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
        for num,frm,to in trips: # iterate through each trips
            while heap and heap[0][0]<=frm: #before picking up the passenger first drop off the current passenger if the current pickup location is there dropoff location
                _,n=heapq.heappop(heap) # pop ou the earliest drop-off
                current-=n #remove the passsengers of the previous ride
            current+=num #add the new passennger
            if current>capacity: #check the capacity
                return False
            heapq.heappush(heap,(to,num)) #add the trip to the heap
        return True # if all the trip are done within the capacity 
