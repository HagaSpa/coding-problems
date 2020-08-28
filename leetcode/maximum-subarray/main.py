class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')     # 全てのループにおける最大値
        current_max_sum = 0         # 現在のループにおける最大値
        for n in nums:
            current_max_sum = max(n, current_max_sum + n)
            max_sum = max(current_max_sum, max_sum)
        return max_sum