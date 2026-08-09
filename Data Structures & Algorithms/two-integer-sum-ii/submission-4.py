class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        while l<r:
            sum_of_numbers=numbers[l]+numbers[r]
            if sum_of_numbers==target:
                return [l+1,r+1]
            elif sum_of_numbers>=target:
                r-=1
            elif sum_of_numbers<=target:
                l+=1
            
            