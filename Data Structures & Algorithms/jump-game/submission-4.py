from functools import cache
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        @cache
        def dfs(ind, l):
            if(ind>=len(nums)-1):
                return True
            isValid=False
            for i in range(1, nums[ind]+1):
                isValid = isValid or dfs(ind+i, i)

            return isValid
        return dfs(0,nums[0])