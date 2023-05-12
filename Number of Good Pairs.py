class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
       my_dict={}

       n_goodPairs =0

       for num in nums:
            if num in my_dict:
               n_goodPairs =  n_goodPairs+ my_dict[num]
               my_dict[num]=my_dict[num]+1
            else:
                my_dict[num]=1
       return n_goodPairs
