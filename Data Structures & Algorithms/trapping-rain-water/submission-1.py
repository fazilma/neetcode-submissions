class Solution:
    def trap(self, height: List[int]) -> int:
        l , r = 0, len(height)-1

        water =0
        l_max =height[l]
        r_max = height[r]
        while(l<r):

            if(l_max < r_max):
                #settle on left , update l
                water += l_max -height[l]
                l+=1
            else:
                water += r_max - height[r]
                r-=1
            l_max = max(height[l], l_max)
            r_max = max(height[r], r_max)
        return water
