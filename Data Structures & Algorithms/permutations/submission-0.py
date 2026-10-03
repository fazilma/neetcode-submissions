class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(arr):
            if (len(arr)==len(nums)):
                res.append(arr[:])
                return
            
            for j in range(len(nums)):
                if(nums[j] in arr):
                    continue
                arr.append(nums[j])
                dfs(arr)
                arr.pop()
        dfs([])
        return res