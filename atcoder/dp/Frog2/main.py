from typing import List


def calc_min_cost(n: int, k: int, h: List[int]) -> int:
    dp = [float('inf')]*n
    dp[0] = 0
    dp[1] = abs(h[1]-h[0])

    """
    iがコストを計算する現在の足場
    jが現在の足場-k番目までのコストを計算するためのindex
    """
    for i in range(2,n):
        for j in range(max(0,i-k),i):
            if dp[i] > dp[j] + abs(h[i]-h[j]):
                dp[i] = dp[j] + abs(h[i]-h[j])
    return dp[-1]


if __name__ == "__main__":
    n,k = (map(int, input().split(" ")))
    h = list(map(int, input().split(" ")))
    ans = calc_min_cost(n=n, k=k, h=h)
    print(ans)