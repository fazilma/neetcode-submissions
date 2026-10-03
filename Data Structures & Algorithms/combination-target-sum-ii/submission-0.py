class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res =[]
        candidates.sort()
        def dfs(arr, start, s):
            if(s>target):
                return
            if(s == target): 
                res.append([candidates[x] for x in arr])
                return

            prev = None
            for i in range(start, len(candidates)):
                if i in arr :
                    continue
                if (prev is not None and prev==candidates[i]):
                    continue
                prev = candidates[i]
                s = sum([candidates[x] for x in arr])
                if(s+candidates[i]> target):
                    break
                dfs(arr+[i], i+1, s+candidates[i])

        dfs([],0, 0)
        return res