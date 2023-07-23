import sys

n, k = map(int, sys.stdin.readline().split())

w_v = []
for i in range(n):
    w_v.append(tuple(map(int, sys.stdin.readline().split())))

ans = 0
dp = [0]*(k+1)
for weight, value in w_v:
    for i in range(k, weight-1, -1):
        dp[i] = max(dp[i], dp[i-weight] + value)

sys.stdout.write(f'{dp[-1]}')
