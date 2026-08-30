class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a hashtable with the frequencies
        frequentTable = {}
        for num in nums:
            frequentTable[num] = 1 + frequentTable.get(num, 0)
        
        
        # create a minheap with the all the frequencies
        heap = []
        for num in frequentTable.keys():
            heapq.heappush(heap, (frequentTable[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        # top k frequent
        topFrequent = []
        while heap:
            topFrequent.append(heapq.heappop(heap)[1])
        
        return topFrequent