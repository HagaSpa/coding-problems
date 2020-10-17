from typing import List


def calc_max_happiness(n: int, act: List[List]) -> int:
    """
    dp[i][k]がi-1日時点で,kを選択した時の最大幸福数
    j==kだと前日~当日で同じ活動を選んだことになるので、それは認められていない
    """
    dp = []
    for i in range(n+1):
        dp.append([0]*3)

    for i in range(n):
        for j in range(3):
            for k in range(3):
                """
                dp[i+1][k]に値を入れるのが目的
                """
                if j==k: continue
                dp[i+1][k] = max(dp[i+1][k], dp[i][j]+act[i][k])
    return max(dp[n])


if __name__ == "__main__":
    n = int(input())
    act = []
    for i in range(n):
        a = list(map(int, input().split(" ")))
        act.append(a)
    ans = calc_max_happiness(n=n, act=act)
    print(ans)