class Solution:
    def scoreOfString(self, s: str) -> int:
        sum=0
        l=0
        r=1
        while r<len(s):
            sum+=abs(ord(s[l])-ord(s[r]))
            l+=1
            r+=1

        return sum

        