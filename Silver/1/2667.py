import sys

n = int(sys.stdin.readline())

offset = [(0, 1), (1, 0), (0, -1), (-1, 0)]

ans = []
graph = []
for i in range(n):
    graph.append(list(sys.stdin.readline().strip()))


for y in range(n):
    for x in range(n):
        if graph[y][x] == '1':
            cnt = 1
            stk = [(x, y)]
            graph[y][x] = '0'
            while len(stk) != 0:
                sts = False
                for x_off, y_off in offset:
                    if 0 <= x_off + stk[-1][0] <= n - 1 and 0 <= y_off + stk[-1][1] <= n -1:
                        if graph[y_off + stk[-1][-1]][x_off + stk[-1][0]] == '1':
                            graph[y_off + stk[-1][1]][x_off + stk[-1][0]] = '0'
                            cnt += 1
                            sts = True
                            stk.append((x_off + stk[-1][0], y_off + stk[-1][1]))
                            break
                
                if sts == False:
                    stk.pop(-1)

            ans.append(cnt)

sys.stdout.write(f'{len(ans)}\n')

ans.sort()
for i in ans:
    sys.stdout.write(f'{i}\n')
