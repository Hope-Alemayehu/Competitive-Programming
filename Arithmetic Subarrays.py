class Solution:
    @staticmethod
    def is_common_difference(nums):
        diff = set({})
        nums = sorted(nums)
        for i in range(1,len(nums)):
            diff.add(nums[i]-nums[i-1])
            if len(diff)>1:
                return False
        return True
        
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        return [ self.is_common_difference(nums[x:y+1]) for x,y in zip(l,r) ]
        print(arithmetic, i, output)
        return output
