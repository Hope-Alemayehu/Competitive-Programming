class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)   #o(n) only have to compute this once
        leftSum =0

        for i in range (len(nums)):
            rightSum = total - nums[i] - leftSum
            if leftSum == rightSum :
                return i
            leftSum += nums[i]
        return -1
        
        #overall time complexity = 0(n)
