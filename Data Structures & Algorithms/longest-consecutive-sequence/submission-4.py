class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_consecutive=1
        counter=1
        nums=sorted(nums)
        print(nums)
        if not nums:
            return 0
        for i in range(1,len(nums)):
            if nums[i-1]+1==nums[i]:
                counter+=1
            elif nums[i-1]==nums[i]:
                pass
            else:
                counter=1
            max_consecutive=max(max_consecutive,counter)
        return max_consecutive