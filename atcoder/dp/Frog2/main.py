from typing import List


def calc_min_cost(n: int, k: int, h: List[int]) -> int:
    dp = [float('inf')]*n
    dp[0] = 0
    """
    iが現在の足場
    jが足場からk番目までのコストをそれぞれ計算するためのindex
    """
    for i in range(0,n):
        for j in range(1,k+1):
            dest = i+j
            if dest>=len(h): continue
            cost = dp[i] + abs(h[dest]-h[i])
            dp[dest] = min(cost, dp[dest])
    return dp[-1]


if __name__ == "__main__":
    n,k = (map(int, input().split(" ")))
    h = list(map(int, input().split(" ")))
    ans = calc_min_cost(n=n, k=k, h=h)
    print(ans)