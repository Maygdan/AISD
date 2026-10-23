n = int(input())

previous, current = 1, 1
for _ in range(n - 1):
    previous, current = current, (previous + current) % 10

print(current)