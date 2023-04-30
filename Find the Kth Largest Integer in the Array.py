class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
       
       val = [ int(x) for x in nums ] 
       val.sort(reverse=True)
       return str(val[k-1])
