from typing import List


class Solution:
    """
    Brute Force

    Time Limit Exceeded...
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.recursive(nums=nums, prev=float('-inf'), i=0)

    def recursive(self, nums, prev, i):
        if i >= len(nums):
            return 0
        cnt = 0
        if prev < nums[i]:
            cnt = 1 + self.recursive(nums=nums, prev=nums[i], i=i+1)
        cnt2 = self.recursive(nums=nums, prev=prev, i=i+1)
        return cnt if cnt > cnt2 else cnt2


if __name__ == "__main__":
    inp = [10,9,2,5,3,7,101,18]
    s = Solution()
    ans = s.lengthOfLIS(nums=inp)
    print(ans)