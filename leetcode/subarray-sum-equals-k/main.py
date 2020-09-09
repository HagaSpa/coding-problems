from typing import List
from collections import Counter


class Solution:
    """
    numsの連続する要素の合計がkとなる部分配列が、幾つ存在するかを返却する。
    
    tableのkeyが部分配列の合計値。この合計値がkのものがいくつあるかを返却する。
    そのためtable[tmp-k]がtable[0]になるなら、そのvalueをcountへ加算する。（valueは個数なので必ず1つ）
    その後その部分配列とkeyにして、1を加算する
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        tmp = 0
        count = 0
        table = Counter()
        table[tmp] = 1
        for num in nums:
            tmp += num
            # kと同じ合計値なら1を加算。ないなら0
            count += table[tmp - k]
            # 合計値hashへセット.
            # [0,0]なら部分配列は[0],[0,0],[0]の三通りあるので、1をインクリメントする 
            table[tmp] += 1                
        return count


if __name__ == "__main__":
    # nums = [1,1,1]
    # k = 2
    # nums = [1,2,1,2,1]
    # k = 3
    # nums = [1,2,3]
    # k = 3

    nums = [0,0,0,0,0,0,0,0,0,0]
    k = 0
    s = Solution()
    ans = s.subarraySum(nums=nums, k=k)
    print(ans)