class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        max_left_height=0
        total_water=0
        max_right_height=[]
        max_height=0
        for i in range(n-1,-1,-1):
            max_height=max(max_height,height[i])
            max_right_height.append(max_height)
        for i in range(n):
            if height[i]<max_left_height and height[i]<max_right_height[n-i-1]:
                water=min(max_right_height[n-i-1],max_left_height)-height[i]
                total_water+=water
            else:
                pass
            max_left_height=max(max_left_height,height[i])
        print(max_right_height[n-2])
        return total_water