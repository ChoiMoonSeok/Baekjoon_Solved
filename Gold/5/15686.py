import sys
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())

mat = []
for i in range(n):
    mat.append(list(map(int, input().split())))

chickens = []
houses = []
for i in range(n):
    for j in range(n):
        if mat[i][j] == 1:
            mat[i][j] = []
            houses.append((i, j))
        elif mat[i][j] == 2:
            chickens.append((i, j))

for y, x in houses:
    for i in chickens:
        mat[y][x].append(abs(i[0] - y) + abs(i[1] - x))

ans = 2 * n * n * n
for i in range(1, m + 1):
    cases = combinations(range(len(chickens)), i)
    for case in cases:
        tmp = 0
        for house in houses:
            tmp += min([mat[house[0]][house[1]][i] for i in case])
        if tmp < ans:
            ans = tmp

print(ans)
