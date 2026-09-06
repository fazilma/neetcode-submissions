class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = {}
        for c in s:
            m[c] = m.get(c,0) +1
        
        for ci in t:
            if ci not in m:
                return False
            m[ci] = m[ci]-1
            if(m[ci]==0):
                del m[ci]
        if len(m) >0:
            return False
        return True