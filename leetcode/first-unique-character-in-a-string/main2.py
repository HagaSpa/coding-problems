class Solution:
    def firstUniqChar(self, s: str) -> int:
        f=len(s)
        for c in string.ascii_lowercase:
            l=s.find(c)
            if l!=-1 and l==s.rfind(c):
                f=min(l,f)
        return f if f!=len(s)else-1
