from typing import List


def calc_max_value(n: int, w: int, items: List[List[int]]):
    """
    AC
    """
    dp = [[0]*w for i in range(n)]
    for i in range(n):
        for j in range(w):
            # 現在の品物の重さがjに収まらない時
            # 前回の品物における最大値をいれる？グリッドにおける１つ上の値
            if j+1<items[i][0]:
                dp[i][j] = dp[i-1][j]
                continue

            # 前の最大値
            prev = 0
            if i>=0:
                prev = dp[i-1][j]

            # 現在の品物の価値
            v = items[i][1]
            
            # 残りスペースにおける最大値
            amount = 0
            if i>=0 and j-items[i][0]>=0:
                amount = dp[i-1][j-items[i][0]]

            dp[i][j] = max(prev, v+amount)

    return dp[-1][-1]


if __name__ == "__main__":
    n,w = map(int, input().split(" "))
    items = [list(map(int, input().split())) for i in range(n)]
    ans = calc_max_value(n=n, w=w, items=items)
    print(ans)