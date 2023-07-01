import sys

n = int(sys.stdin.readline())

rgb = [[i for i in map(int, sys.stdin.readline().split())] for i in range(n)]


dp = [[0] * 3 for i in range(n)]
dp[0][0] = rgb[0][0]
dp[0][1] = rgb[0][1]
dp[0][2] = rgb[0][2]

for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rgb[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + rgb[i][1]
    dp[i][2] = min(dp[i-1][1], dp[i-1][0]) + rgb[i][2]

sys.stdout.write(f'{min(dp[-1])}\n')
