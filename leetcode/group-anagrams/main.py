from typing import List
from collections import Counter
from collections import defaultdict


class Solution:
    """
    groupAnagrams return a list of anagram in strs.
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            ans[tuple(sorted(Counter(s).items()))].append(s)
        return ans.values()



# Entry point for debug
if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    s = Solution()
    ans = s.groupAnagrams(strs=strs)
    print(ans)