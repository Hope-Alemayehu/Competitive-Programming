class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
       #to check the length of the original array
        if len(changed) % 2 != 0:
            return []
        #initalizing directory to keep track offrequency of each element
        freq = {}
        #how we keep track of the freuency of elements
        for num in changed:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        result = []
        
        for num in sorted(freq.keys()):
            if num * 2 in freq and freq[num] > 0 and freq[num * 2] > 0:
                result.append(num)
                freq[num] -= 1
                freq[num * 2] -= 1
        for count in freq.values():
            if count > 0:
                return []
        return result
    
    
    
