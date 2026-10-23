import sys

data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
prefix = data[1:n + 1]
z = [0] * n

for end in range(1, n):
    border_length = prefix[end]
    if border_length:
        start = end - border_length + 1
        z[start] = max(z[start], border_length)

left = 0
right = 0
for i in range(1, n):
    if i < right:
        z[i] = max(z[i], min(right - i, z[i - left]))

    if i + z[i] > right:
        left = i
        right = i + z[i]

sys.stdout.write(" ".join(map(str, z)))