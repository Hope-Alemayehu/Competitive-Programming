import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Step 1: Create a hash map
        count_map = defaultdict(int)
        for num in nums:
            count_map[num] += 1
        
        # Step 2: Create a min heap of size K
        heap = []
        for num, count in count_map.items():
            if len(heap) < k:
                heapq.heappush(heap, (count, num))
            else:
                heapq.heappushpop(heap, (count, num))
        
        # Step 3: Create an output array
        output = []
        while heap:
            output.append(heapq.heappop(heap)[1])
        
        # Step 4: Return the output array
        return output[::-1]
