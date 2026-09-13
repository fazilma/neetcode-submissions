class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            seen = set()
            prev_j=None
            if (i>0 and nums[i]==nums[i-1]):
                continue

            for j in range(i+1, len(nums)):
                if (prev_j is not None and nums[j]==prev_j):
                    continue
                target = 0-nums[i]-nums[j]
                if target in seen:
                        res.append([nums[i],nums[j], target])
                        prev_j = nums[j]
                seen.add(nums[j])
        return res