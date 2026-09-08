class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [1] * n

        for i in range(n):
            out[i] = out[i-1] * nums[i] if i>0 else nums[i]
        post = 1
        for i in range(n-1,-1,-1):
            out[i] = out[i-1] *  post if i>0 else post
            post = post * nums[i]
        
        return out