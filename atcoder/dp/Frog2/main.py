from typing import List


def calc_min_cost(n: int, k: int, h: List[int]) -> int:
    dp = [float('inf')]*n
    dp[0] = 0
    for i in range(1,n):
        if i<k:
            for j in range(i):
                cost = dp[j] + abs(h[i]-h[j])
                dp[i] = min(cost, dp[i])
            continue
        for ik in range(i-k, i):
            cost = dp[ik] + abs(h[i]-h[ik])
            dp[i] = min(cost, dp[i])
    return dp[-1]


if __name__ == "__main__":
    n,k = (map(int, input().split(" ")))
    h = list(map(int, input().split(" ")))
    ans = calc_min_cost(n=n, k=k, h=h)
    print(ans)