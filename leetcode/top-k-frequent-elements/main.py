from typing import List
import collections


class Solution:
    """
    topKFrequesnt returns a list of the top k frequency values in nums.
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = collections.Counter(nums)
        cc = c.most_common(n=k)
        li = [c[0] for c in cc]
        return li


# Entry point for debug
if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2
    s = Solution()
    ans = s.topKFrequent(nums=nums, k=k)
    print(ans)