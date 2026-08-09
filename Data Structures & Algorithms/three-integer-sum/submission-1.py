class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums_sorted=sorted(nums)
        for i in range(len(nums)-2):
            if i>0 and nums_sorted[i] == nums_sorted[i - 1]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                three_sum=nums_sorted[i]+nums_sorted[l]+nums_sorted[r]
                if three_sum==0:
                    res.append([nums_sorted[i],nums_sorted[l],nums_sorted[r]])
                    while l < r and nums_sorted[l] == nums_sorted[l + 1]:
                        l += 1
                    while l < r and nums_sorted[r] == nums_sorted[r - 1]:
                        r -= 1
                    l+=1
                    r-=1
                elif three_sum>0:
                    r-=1
                elif three_sum<0:
                    l+=1
        return res

        