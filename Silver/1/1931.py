import sys

n = int(sys.stdin.readline())

cases = dict()
ends = []
for i in range(n):
    stt, end = map(int, sys.stdin.readline().split())
    ends.append(end)
    if end not in cases:
        cases[end] = [stt]
    else:
        cases[end].append(stt)

ends.sort()
for i in cases:
    cases[i].sort()

time = 0
ans = 0
for end in ends:
    for i in cases[end]:
        if i >= time:
            ans += 1
            time = end
            break

sys.stdout.write(f'{ans}')
