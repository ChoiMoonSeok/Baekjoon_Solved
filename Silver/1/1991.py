import sys

n = int(sys.stdin.readline())

graph = dict()
for i in range(n):
    tmp = sys.stdin.readline().strip().split()
    graph[tmp[0]] = tmp[1:]

stk = ["A"]
vit = {"A"}
sys.stdout.write("A")
while len(stk) > 0:
    if graph[stk[-1]][0] != "." and graph[stk[-1]][0] not in vit:
        sys.stdout.write(f"{graph[stk[-1]][0]}")
        vit.add(graph[stk[-1]][0])
        stk.append(graph[stk[-1]][0])
    else:
        if graph[stk[-1]][1] != "." and graph[stk[-1]][1] not in vit:
            sys.stdout.write(f"{graph[stk[-1]][1]}")
            vit.add(graph[stk[-1]][1])
            stk.append(graph[stk[-1]][1])
        else:
            stk.pop(-1)

sys.stdout.write("\n")

stk = ["A"]
vit = set()
while len(stk) > 0:
    if graph[stk[-1]][0] != "." and graph[stk[-1]][0] not in vit:
        stk.append(graph[stk[-1]][0])
    else:
        if graph[stk[-1]][1] != "." and graph[stk[-1]][1] not in vit:
            sys.stdout.write(f"{stk[-1]}")
            vit.add(stk[-1])
            stk.append(graph[stk[-1]][1])
        else:
            if stk[-1] not in vit:
                sys.stdout.write(f"{stk[-1]}")
                vit.add(stk[-1])
            stk.pop(-1)

sys.stdout.write("\n")

stk = ["A"]
vit = set()
while len(stk) > 0:
    if graph[stk[-1]][0] != "." and graph[stk[-1]][0] not in vit:
        stk.append(graph[stk[-1]][0])
    else:
        if graph[stk[-1]][1] != "." and graph[stk[-1]][1] not in vit:
            stk.append(graph[stk[-1]][1])
        else:
            sys.stdout.write(f"{stk[-1]}")
            vit.add(stk[-1])
            stk.pop(-1)
