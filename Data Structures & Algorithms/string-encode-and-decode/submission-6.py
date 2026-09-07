class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for word in strs:
            res.append(str(len(word)))
            res.append("#")
            res.append(word)
        ret = ''.join(res)
        return ret


    def decode(self, s: str) -> List[str]:
        out = []
        i,j = 0,0
        while(i<len(s)):
            j=i
            num = 0
            while(s[j] != '#'):
                j +=1
            num = int(s[i:j])
            out.append(s[j+1:j+num+1])
            i = j + num +1
        return out
            



                




