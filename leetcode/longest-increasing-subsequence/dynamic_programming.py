from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        if not nums:return 0
        
        # initializing
        dp = [1]*len(nums)
        
        res = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i] = max(dp[i],dp[j]+1)
        
        return max(dp)


if __name__ == "__main__":
    inp = [10,9,2,5,3,7,101,18]
    s = Solution()
    ans = s.lengthOfLIS(nums=inp)
    print(ans)