from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(lambda :0)
        for num in nums:
            d[num] +=1
        
        maxH = []
        for key,val in d.items():
            heapq.heappush(maxH, (-val, key))
        
        res =[]
        for j in range(k):
            ele = heapq.heappop(maxH)
            res.append(ele[1])
        return res