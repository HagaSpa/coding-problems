class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i,v in enumerate(s):
            if s.count(v) == 1:
                return i
        return -1

    
if __name__ == "__main__":
    inp = "leetcode"
    # inp = "cc"
    s = Solution()
    ans = s.firstUniqChar(s=inp)
    print(ans)