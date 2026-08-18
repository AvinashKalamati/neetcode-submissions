class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk=[]
        max_area=0
        for p,h in enumerate(heights):
            start=p
            while stk and stk[-1][1]>h:
                popped_pos,popped_height=stk.pop()
                max_area=max(max_area,popped_height*(p-popped_pos))
                start=popped_pos
            stk.append((start,h))
        for p,h in stk:
            max_area=max(max_area,h*(len(heights)-p))
        return max_area

                


        