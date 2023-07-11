import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())

mat = []
vit = [[False]*m for i in range(n)]
que = deque([])
for i in range(n):
    tmp = sys.stdin.readline().strip().split()
    for j in range(m):
        if tmp[j] == '1':
            que.append([i, j])
            vit[i][j] = True
        elif tmp[j] == '-1':
            vit[i][j] = True


direction = ((0, 1), (0, -1), (1, 0), (-1, 0))

ans = -1
while len(que) != 0:
    for cordinate in range(len(que)):
        cordinate_y, cordinate_x = que.popleft()
        for d_y, d_x in direction:
            if (0 <= cordinate_y + d_y < n) and (0 <= cordinate_x + d_x < m): 
                if vit[cordinate_y + d_y][cordinate_x+d_x] == False:
                    vit[cordinate_y + d_y][cordinate_x+d_x] = True
                    que.append([cordinate_y + d_y, cordinate_x+d_x])
    ans += 1

for i in range(n):
    for j in range(m):
        if vit[i][j] == False:
            sys.stdout.write('-1')
            exit(0)        

sys.stdout.write(f'{ans}')
