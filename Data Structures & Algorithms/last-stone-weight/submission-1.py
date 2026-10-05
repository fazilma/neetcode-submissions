class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while(len(stones)>1):
            one = stones.pop()
            two = stones.pop()
            if(one==two):
                continue
            diff = abs(one-two)
            i = 0
            while(i<len(stones) and diff > stones[i]):
                i+=1
            stones.insert(i, diff)
        return (stones and stones[0]) or 0