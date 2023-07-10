n = int(input())
Ps = list(map(int, input().split()))
Ps.insert(0, 0)

dp = [0] * (n+1)
for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(Ps[j] + dp[i-j], dp[i])

print(dp[-1])
