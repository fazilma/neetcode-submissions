class Solution:
    def trap(self, height: List[int]) -> int:
        left_bound = [i for i in height]
        right_bound = [i for i in height]
        prev = 0
        for i in range(len(height)):
            left_bound[i] = max(height[i], left_bound[i-1] if i>0 else 0)
        for i in range(len(height)-1, -1,-1):
            right_bound[i] = max(height[i], right_bound[i+1] if i+1<len(height) else 0)

        water = 0
        for i in range(len(height)):
            water += abs((height[i]- (min(left_bound[i], right_bound[i]))))
        return water