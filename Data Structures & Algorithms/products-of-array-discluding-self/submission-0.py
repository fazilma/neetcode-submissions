class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums) 
        
        p=len(nums)-2
        while(p>=0):
            left[p] = nums[p+1] * left[p+1]
            p -=1
        p=1
        while(p<len(nums)):
            right[p] = right[p-1] * nums[p-1]
            p +=1
        for i in range(len(nums)):
            left[i] = left[i] * right[i]
        return left