class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = set(nums)
        i =0
        maxL = 0
        long_set = set()
        while(i < len(nums)):
            num = nums[i]
            if num in long_set:
                i +=1
                continue
            s = set()
            s.add(num)
            lenL =1
            while (num +1 in m):
                lenL +=1
                s.add(num+1)
                num = num+1
            if lenL > maxL:
                maxL = lenL
                long_set = s.copy()
            i +=1
            
        return maxL