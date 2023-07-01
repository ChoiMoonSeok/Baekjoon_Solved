import sys

n = int(sys.stdin.readline())

ans = []


def hanoi(n, a, b, c):
    global ans
    if n == 1:
        ans.append((a, c))
    else:
        hanoi(n - 1, a, c, b)
        ans.append((a, c))
        hanoi(n - 1, b, a, c)


hanoi(n, 1, 2, 3)

sys.stdout.write(f"{len(ans)}\n")

for i in ans:
    sys.stdout.write(f"{i[0]} {i[1]}\n")
