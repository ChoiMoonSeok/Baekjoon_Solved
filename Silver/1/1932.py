import sys

n = int(sys.stdin.readline())

dp = [[0] * i for i in range(1, n + 1)]
dp[0][0] = int(sys.stdin.readline())
for i in range(1, n):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(i + 1):
        if 0 < j < i:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + tmp[j]
        elif j == 0:
            dp[i][j] = dp[i-1][j] + tmp[j]
        else:
            dp[i][j] = dp[i-1][j-1] + tmp[j]

sys.stdout.write(f'{max(dp[-1])}')
