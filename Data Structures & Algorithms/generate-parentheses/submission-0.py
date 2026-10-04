class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res =[]
        def dfs(comb, open_p, close_p):
            if(open_p==close_p and close_p==n):
                res.append(comb)
                return
            
            if(open_p <n):
                dfs(comb+'(', open_p+1, close_p)
            
            if(close_p < open_p):
                dfs(comb+')', open_p, close_p+1)
            
        dfs('', 0, 0)
        return res

        