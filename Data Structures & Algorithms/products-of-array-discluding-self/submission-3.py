class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        right = [1] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            right[i] = right[i+1] * nums[i] if i<len(nums)-1 else nums[i]
        prod = 1
        for i in range(len(nums)):
            res[i] = prod * right[i+1] if i<len(nums)-1 else prod
            prod = prod * nums[i]

        return res