class Solution:
    def maxArea(self, heights):
        n=len(heights)
        left=0
        right=n-1
        max_area=0
        while left<right:
            w=right-left
            h=min(heights[left],heights[right])
            max_area=max(max_area,w*h)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return max_area
