import sys

n = int(sys.stdin.readline())

video = []
for i in range(n):
    video.extend([int(i) for i in sys.stdin.readline().strip()])


def div1(data, n):
    tmp = []
    for i in range(n // 2):
        tmp.extend(data[n * i : n // 2 + n * i])
    return tmp


def div2(data, n):
    tmp = []
    for i in range(n // 2):
        tmp.extend(data[n * i + n // 2 : n * (i + 1)])
    return tmp


def div3(data, n):
    tmp = []
    for i in range(n // 2, n):
        tmp.extend(data[n * i : n // 2 + n * i])
    return tmp


def div4(data, n):
    tmp = []
    for i in range(n // 2, n):
        tmp.extend(data[n * i + n // 2 : n * (i + 1)])
    return tmp


def div_con(data, n):
    if len(set(data)) > 1:
        return (
            "("
            + div_con(div1(data, n), n // 2)
            + div_con(div2(data, n), n // 2)
            + div_con(div3(data, n), n // 2)
            + div_con(div4(data, n), n // 2)
            + ")"
        )
    else:
        return str(data[0])


sys.stdout.write(f"{div_con(video, n)}")
