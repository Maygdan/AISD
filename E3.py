import sys

s = sys.stdin.buffer.readline().strip()
n = len(s)
z = [0] * n
left = 0
right = 0
answer = 0

for i in range(1, n):
    if i < right:
        z[i] = min(right - i, z[i - left])

    while i + z[i] < n and s[z[i]] == s[i + z[i]]:
        z[i] += 1

    if i + z[i] > right:
        left = i
        right = i + z[i]

    answer = max(answer, min(z[i], i))

print(answer)