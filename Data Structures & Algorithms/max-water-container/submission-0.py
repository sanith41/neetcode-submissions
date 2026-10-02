class Solution:
    def maxArea(self, heights: List[int]) -> int:
        j=len(heights)-1
        i=0
        max=0
        
        while i<j:
            if heights[i]>heights[j]:
                res=heights[j]*(j-i)
                if res>max:
                    max=res
                j=j-1
            else:
                res=heights[i]*(j-i)
                if res>max:
                    max=res
                i=i+1
        return max
            
        