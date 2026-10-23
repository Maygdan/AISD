import sys

data = list(map(int, sys.stdin.buffer.read().split()))
n, p, m = data[:3]
values = data[3:3 + n]

hash_value = 0
for value in values:
    hash_value = (hash_value * p + value) % m

print(hash_value)