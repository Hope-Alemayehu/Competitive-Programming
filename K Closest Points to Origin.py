class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #to store distance and the coordinates
        minHeap=[]
        #to calculate the distance and add that to the minHeap array
        for x,y in points:
            dist = (x**2) +(y**2)
            minHeap.append([dist,x,y])
        #heapify function to convert minHeap list into heap data structure
        heapq.heapify(minHeap)
        #to store the final result
        res=[]
        #to extract the minimum distance and corrsponding x and y coordinates
        while k>0:
            dist,x,y=heapq.heappop(minHeap)
            #removing the distance
            res.append([x,y])
            k-=1
        return res
