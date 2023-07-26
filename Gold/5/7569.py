import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())

que = deque()
box = []
for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int, sys.stdin.readline().split())))
        for k in range(m):
            if tmp[-1][k] == 1:
                que.append((k, j, i))
    box.append(tmp)

direction = [(0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0)]

cnt = -1
while len(que) != 0:
    cnt += 1
    tmp = deque()
    for i in range(len(que)):
        sts = que.popleft()
        for x, y, z in direction:
            if 0 <= sts[0] + x < m and 0 <= sts[1] + y < n and 0 <= sts[2] + z < h:
                if box[sts[2] + z][sts[1] + y][sts[0] + x] == 0:
                    tmp.append((sts[0] + x, sts[1] + y, sts[2] + z))
                    box[sts[2] + z][sts[1] + y][sts[0] + x] = 1
    que = tmp


def chk_0(box):
    for i in box:
        for j in i:
            for k in j:
                if k == 0:
                    return 0
    return 1


if chk_0(box) == 0:
    sys.stdout.write("-1")
else:
    sys.stdout.write(f"{cnt}")
