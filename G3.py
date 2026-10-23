import sys

data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
z = data[1:n + 1]
prefix = [0] * n

for i in range(1, n):
    position = i + z[i] - 1
    while position >= i and prefix[position] == 0:
        prefix[position] = position - i + 1
        position -= 1

sys.stdout.write(" ".join(map(str, prefix)))