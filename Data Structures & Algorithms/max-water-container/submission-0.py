class Solution:
    def maxArea(self, heights: List[int]) -> int:
        h1=heights[0]
        h2=heights[-1]
        l=0
        r=len(heights)-1
        area = (r-l)*min(h1,h2)
        while l<r:
            if h1<=h2:
                l+=1
                h1 = heights[l]
            else:
                r-=1
                h2 = heights[r]
            new_area = (r-l)*min(h1,h2)
            if new_area>area:
                area=new_area
        
        return area


        