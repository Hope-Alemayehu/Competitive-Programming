class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []

        left, right = 0, len(nums)-1
        while len(res) != len(nums):
            res.append(nums[left])
            left += 1
            if left <= right:
                res.append(nums[right])
                right -= 1
        
        return res
        
        
