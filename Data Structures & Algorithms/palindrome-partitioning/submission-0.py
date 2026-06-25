class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        res=[]
        path=[]
        def f(start):
            if start==len(s):
                res.append(path[:])
                return
            def ispalindrome(curr):
                return curr==curr[::-1]
            for end in range(start,n):
                curr=s[start:end+1]
                if not ispalindrome(curr):
                    continue
                path.append(curr)
                f(end+1)
                path.pop()
        f(0)
        return res