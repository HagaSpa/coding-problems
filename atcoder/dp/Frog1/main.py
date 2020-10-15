from typing import List


def calc_min_cost(n: int, h: List[int]) -> int:
    dp = [float('inf')]*n
    dp[0] = 0
    for i in range(1,n):
        if i==1:
            dp[i] = abs(h[i]-h[i-1])
            continue
        skip_one = dp[i-1] + abs(h[i]-h[i-1])
        skip_two = dp[i-2] + abs(h[i]-h[i-2])
        dp[i] = min(skip_one, skip_two)
    return dp[-1]


if __name__ == "__main__":
    n = int(input())
    h = list(map(int, input().split(" ")))
    ans = calc_min_cost(n=n, h=h)
    print(ans)