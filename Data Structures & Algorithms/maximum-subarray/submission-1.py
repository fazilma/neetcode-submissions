class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s_max =nums[0]
        s=0
        for i in nums:
            if(s<0):
                s=0
            s +=i
            s_max = max(s_max, s)
        return s_max