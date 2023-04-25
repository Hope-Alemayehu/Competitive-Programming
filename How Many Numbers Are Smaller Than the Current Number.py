class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sortednums = sorted(nums)
        dic= {}
        result= []
        for i in range (len(sortednums)):
            if sortednums[i] not in dic:
                dic[sortednums[i]]=i
        for i in nums:
            result.append(dic[i])
        return result
