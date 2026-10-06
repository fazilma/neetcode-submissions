class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        l, r = 0, 0
        max_l = 0

        while(l<=r and r<len(s)):
            if(s[r] not in m):
                
                max_l = max(r-l+1, max_l)
                m[s[r]] = m.get(s[r], 0)+1
                r+=1
            elif(s[r] in m):
                
                m[s[l]] = m[s[l]]-1
                if( m[s[l]] ==0):
                    del  m[s[l]]
                l+=1
        return max_l