import sys

s = sys.stdin.buffer.readline().strip()
prefix = [0] * len(s)

for i in range(1, len(s)):
    border_length = prefix[i - 1]
    while border_length > 0 and s[i] != s[border_length]:
        border_length = prefix[border_length - 1]
    if s[i] == s[border_length]:
        border_length += 1
    prefix[i] = border_length

borders = []
border_length = prefix[-1]
while border_length > 0:
    borders.append(border_length)
    border_length = prefix[border_length - 1]

borders.reverse()
print(len(borders))
if borders:
    print(*borders)