import sys

n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())

mat = []
for i in range(n): 
    mat.append(tuple(map(int, sys.stdin.readline().split())))

def get_direction(d):
    if d == 0:
        return (0, -1)
    elif d == 1:
        return (1, 0)
    elif d == 2:
        return (0, 1)
    else:
        return (-1, 0)

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
cnt = 0
vit = [[False]*m for i in range(n)]
while True:
    if vit[r][c] == False:
        vit[r][c] = True
        cnt += 1
    else:
        sts = False
        for x, y in direction:
            if 0 <= r + y < n and 0 <= c + x < m:
                if mat[r + y][c + x] == 0 and vit[r + y][c + x] == 0:
                    sts = True
                    break
        if sts == True:
            d -= 1
            if d < 0:
                d = 3
            x, y = get_direction(d)
            if 0 <= r + y < n and 0 <= c + x < m:
                if mat[r + y][c + x] == 0 and vit[r + y][c + x] == False:
                    r += y
                    c += x
        else:
            x, y = get_direction(d)
            if 0 <= r - y < n and 0 <= c - x < m:
                if mat[r - y][c - x] == 0: 
                    r -= y
                    c -= x
                else:
                    break
            else:
                break
            

sys.stdout.write(f'{cnt}') 
