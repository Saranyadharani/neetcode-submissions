class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq=Counter(tasks)
        heap=[-count for count in freq.values()]
        heapq.heapify(heap)
        time=0
        while heap:
            temp=[]
            for i in range(n+1):
                if heap:
                    count=-heapq.heappop(heap)
                    if count>1:
                        temp.append(-(count-1))
                    time+=1
                else:
                    if not temp:
                        break
                    time+=1
            for item in temp:
                heapq.heappush(heap,item)
        return time

