from typing import List
from collections import defaultdict

import copy

class Solution:
    """
    Recursion with Memoization

    Time Limit Exceeded...
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        li = [-1 for i in range(len(nums))]
        memo = [copy.deepcopy(li) for i in range(len(nums))]
        return self.recursive(nums=nums, prev=-1, cur=0, memo=memo)

    def recursive(self, nums: List[int], prev: int, cur: int, memo: List[List[int]]):
        # guard infinite loop
        if cur==len(nums):
            return 0
        # checked?
        if memo[prev+1][cur] != -1:
            return memo[prev+1][cur]
        
        # LIS
        cnt = 0
        if prev<0 or nums[cur] > nums[prev]:
            cnt = 1 + self.recursive(nums=nums, prev=cur, cur=cur+1, memo=memo)
        cnt2 = 0
        cnt2 = self.recursive(nums=nums, prev=prev, cur=cur+1, memo=memo)
        memo[prev+1][cur] = cnt if cnt > cnt2 else cnt2
        return memo[prev+1][cur]


if __name__ == "__main__":
    inp = [10,9,2,5,3,7,101,18]
    
    # RecursionError: maximum recursion depth exceeded while calling a Python object
    # import sys
    # sys.setrecursionlimit(50000)
    # inp = list(range(2500))
    
    s = Solution()
    ans = s.lengthOfLIS(nums=inp)
    print(ans)