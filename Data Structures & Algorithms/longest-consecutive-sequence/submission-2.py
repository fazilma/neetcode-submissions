class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = set(nums)
        i =0
        maxL = 0
        not_start = set()
        while(i < len(nums)):
            num = nums[i]
            if num in not_start:
                i+=1
                continue
            lenL =1
            while (num +1 in m):
                lenL +=1
                not_start.add(num+1)
                num = num+1
            if lenL > maxL:
                maxL = lenL
            i +=1
            
        return maxL