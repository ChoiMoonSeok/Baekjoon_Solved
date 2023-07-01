import sys

n = int(sys.stdin.readline())

direction = ((1, 0), (-1, 0), (0, 1), (0, -1))
graph = [[None] * n for i in range(n)]
for i in range(n):
    tmp_cnt = 0
    for j in sys.stdin.readline().strip():
        graph[i][tmp_cnt] = j
        tmp_cnt += 1


def dfs(stk, vit, color):
    global direction, n, graph
    while len(stk) != 0:
        vit[stk[-1][0]][stk[-1][1]] = True
        sts = False
        for x, y in direction:
            if 0 <= stk[-1][0] + x < n and 0 <= stk[-1][1] + y < n:
                if vit[stk[-1][0] + x][stk[-1][1] + y] == False:
                    if graph[stk[-1][0] + x][stk[-1][1] + y] in color:
                        stk.append((stk[-1][0] + x, stk[-1][1] + y))
                        sts = True
                        break
        if sts == False:
            stk.pop(-1)


ans = [0, 0]
vit = [[False] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if vit[i][j] == False:
            dfs([(i, j)], vit, {graph[i][j]})
            ans[0] += 1

vit = [[False] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if vit[i][j] == False:
            if graph[i][j] == "B":
                dfs([(i, j)], vit, {"B"})
                ans[1] += 1
            else:
                dfs([(i, j)], vit, {"G", "R"})
                ans[1] += 1


sys.stdout.write(f"{ans[0]} {ans[1]}")
