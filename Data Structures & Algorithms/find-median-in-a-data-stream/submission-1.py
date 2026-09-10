import heapq
class MedianFinder:

    def __init__(self):
        self.left=[] #stores the smaller values (max heap)
        self.right=[] #stores the larger values (min heap)
        #conditions 1. -len(left)=len(right) or len(right)+1
        # 2. the elements in left heap <=elements in the right heap 

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left,-num)
        #move the largest no from left to right and balance the heap
        heapq.heappush(self.right,-heapq.heappop(self.left))
        #condtion is violated mean do below 
        if len(self.right)>len(self.left):
            heapq.heappush(self.left,-heapq.heappop(self.right))
    def findMedian(self) -> float:
        #if len(left)>len(right) root of the left heap is the median
        if len(self.left)>len(self.right):
            return -self.left[0]
        else:
            return (-self.left[0]+self.right[0])/2.0        
        









#input=[5,15,1,3]


#for i=0 LEFT=[5] RIGHT = EMPTY , i=1 left=[15,5] right=[] it is imbalance move 15 from left to right so left=[5] right=[15] then i=2 left=[5,1] right=[15] the condition of length of left=right or right+1 is violated so move the 5 from left to right we get left=[1] right=[5,15] next i=3 left=[3,1] and right=[5,15] so now the len of the both heap is same and also the element in left heap is less than or rqual to the right heap and now median is average of the top root elemnt of the both heap that left[0]=3 right=[0]=5 so the median is 3+5/2 =4