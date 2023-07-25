# bfs를 활용하여 풀이함
import sys

n, m = map(int, sys.stdin.readline().split())

nodes = dict()
for i in range(n-1):
    tmp = tuple(map(int, sys.stdin.readline().split()))
    if tmp[0] in nodes:
        nodes[tmp[0]].append((tmp[1], tmp[2]))
    else:
        nodes[tmp[0]] = [(tmp[1], tmp[2])]
    if tmp[1] in nodes:
        nodes[tmp[1]].append((tmp[0], tmp[2]))
    else:
        nodes[tmp[1]] = [(tmp[0], tmp[2])]


dis_node = []
for i in range(m):
    dis_node.append(tuple(map(int, sys.stdin.readline().split())))

for stt, end in dis_node:
    ans = {i:10000*n for i in nodes}
    ans[stt] = 0
    que = [stt]
    vit = {i:False for i in nodes} 
    vit[stt] = True
    while len(que) != 0:
        for node, dis in nodes[que[0]]:
            if vit[node] == False:
                que.append(node)
                vit[node] = True
                ans[node] = min(ans[node], ans[que[0]]+dis)
        que.pop(0)

    sys.stdout.write(f'{ans[end]}\n')
