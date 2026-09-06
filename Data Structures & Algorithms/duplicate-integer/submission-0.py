class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = {}
        for i in nums:
            if(a.get(i, 0) >=1):
                return True
            a[i] = a.get(i, 0) + 1
        return False