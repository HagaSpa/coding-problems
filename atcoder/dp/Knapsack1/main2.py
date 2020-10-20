from typing import List


def calc_max_value(n: int, w: int, items: List[List[int]]):
    """
    https://qiita.com/drken/items/dc53c683d6de8aeacf5a#%E3%82%AD%E3%83%BC%E3%83%9D%E3%82%A4%E3%83%B3%E3%83%88-1
    
    上記を参考にしたコード. TLEだけど
    """
    # indexは1から値を入れていくため、縦横１つずつ余分に確保する
    dp = [[0]*(w+1) for i in range(n+1)]
    for i in range(n):
        for j in range(w+1): # 横に1つ増やしているのでw+1. iは+1して処理するのでnはそのまま
            # 容量に収まるなら
            if j - items[i][0] >= 0:
                dp[i+1][j] = max(dp[i][j], items[i][1] + dp[i][j-items[i][0]])
                continue
            dp[i+1][j] = dp[i][j]

    return dp[n][w]


if __name__ == "__main__":
    n,w = map(int, input().split(" "))
    items = [list(map(int, input().split())) for i in range(n)]
    ans = calc_max_value(n=n, w=w, items=items)
    print(ans)