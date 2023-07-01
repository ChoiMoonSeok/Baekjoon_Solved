import sys

n, m = map(int, sys.stdin.readline().split())

vit = [[False] * m for i in range(n)]
graph = [[[] for j in range(m)] for i in range(n)]
prev = [[(-1, -1) for j in range(m)] for i in range(n)]

for y in range(n):
    tmp = sys.stdin.readline().strip()
    for x in range(m):
        if tmp[x] == "1":
            if 0 < x < m - 1:
                graph[y][x].append((x + 1, y))
                graph[y][x].append((x - 1, y))
            elif x == 0:
                graph[y][x].append((x + 1, y))
            else:
                graph[y][x].append((x - 1, y))
            if 0 < y < n - 1:
                graph[y][x].append((x, y - 1))
                graph[y][x].append((x, y + 1))
            elif y == 0:
                graph[y][x].append((x, y + 1))
            else:
                graph[y][x].append((x, y - 1))

que = [(0, 0)]
vit[0][0] = True
sts = False
while len(que) != 0:
    tmp = que.pop(0)
    vit[tmp[1]][tmp[0]] = True
    for i in graph[tmp[1]][tmp[0]]:
        if vit[i[1]][i[0]] == False:
            que.append(i)
            vit[i[1]][i[0]] = True
            prev[i[1]][i[0]] = tmp
        if i == (m - 1, n - 1):
            sts = True
            break

    if sts == True:
        break

stt = (m - 1, n - 1)
cnt = 1
while stt != (0, 0):
    cnt += 1
    stt = prev[stt[1]][stt[0]]

sys.stdout.write(f"{cnt}\n")
