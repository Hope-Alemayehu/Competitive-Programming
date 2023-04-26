class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(nums)
        temp_arr=[]
        for i in range (len(nums)):
            if target == nums[i]:
                temp_arr.append(i)
        return (temp_arr)
