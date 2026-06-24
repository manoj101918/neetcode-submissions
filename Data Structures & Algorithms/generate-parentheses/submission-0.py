class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        curr=""
        def f(open_count,close_count,curr):
            if len(curr)==2*n:
                res.append(curr)
                return
            if open_count<n:
                f(open_count+1,close_count,curr+'(')
            if close_count<open_count:
                f(open_count,close_count+1,curr+')')
        f(0,0,curr)
        return res
        