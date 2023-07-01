import sys
import math

n = int(sys.stdin.readline())

mat = [[1] * n for i in range(n)]

for i in range(int(math.sqrt(n))):
    for j in range(3**i, n, 3 ** (i + 1)):
        for k in range(3**i, n, 3 ** (i + 1)):
            for l in range(3**i):
                mat[j + l][k : k + (3**i)] = [0] * (3**i)

for i in range(n):
    for j in range(n):
        if mat[i][j] == 1:
            sys.stdout.write("*")
        else:
            sys.stdout.write(" ")
    sys.stdout.write("\n")
