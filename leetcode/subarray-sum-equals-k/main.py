from typing import List
from collections import Counter


class Solution:
    """
    numsの連続する要素の合計がkとなる部分配列が、幾つ存在するかを返却する。
    TODO: ロジック腹落ちしてないから、もう少し詳細に
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        tmp = 0
        res = 0
        table = Counter()
        table[tmp] = 1
        for i, num in enumerate(nums):
            tmp += num
            res += table[tmp - k]
            table[tmp] += 1                
        return res


if __name__ == "__main__":
    # nums = [1,1,1]
    # k = 2
    nums = [1,2,1,2,1]
    k = 3

    # nums = [1,2,3]
    # k = 3
    s = Solution()
    ans = s.subarraySum(nums=nums, k=k)
    print(ans)