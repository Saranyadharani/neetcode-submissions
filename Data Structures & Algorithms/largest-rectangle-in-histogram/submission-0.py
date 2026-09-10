class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        stack=[]
        max_area=0
        for i in range(n+1):
            curr_height=heights[i] if i<n else 0 #hadhling sentinel nodes
            while stack and curr_height < heights[stack[-1]]:
                height=heights[stack.pop()]
                width=i if not stack else i- stack[-1] -1
                area=height* width
                max_area=max(area,max_area)
            stack.append(i)
        return max_area
