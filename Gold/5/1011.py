import sys

n = int(sys.stdin.readline())

cases = [[0, 0] for i in range(n)]
for i in range(n):
    cases[i][0], cases[i][1] = map(int, sys.stdin.readline().split())

for x, y in cases:
    dis = y - x
    k = 1
    while k * (k + 1) < dis:
        k += 1

    if k * (k - 1) == dis:
        sys.stdout.write(f"{2 * (k-1)}\n")
    else:
        if dis - k * (k - 1) > k:
            cnt = 1
            while dis - k * (k - 1) - k * cnt > 0:
                cnt += 1
            sys.stdout.write(f"{2*(k-1)+cnt}\n")

        else:
            sys.stdout.write(f"{2*(k-1)+1}\n")
