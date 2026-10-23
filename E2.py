import sys

MOD1 = 1_000_000_007
MOD2 = 1_000_000_009
BASE = 911_382_323

data = sys.stdin.buffer.read().split()
s = data[0]
query_count = int(data[1])

prefix1 = [0] * (len(s) + 1)
prefix2 = [0] * (len(s) + 1)
power1 = [1] * (len(s) + 1)
power2 = [1] * (len(s) + 1)

for i, character in enumerate(s, 1):
    value = character - ord("a") + 1
    prefix1[i] = (prefix1[i - 1] * BASE + value) % MOD1
    prefix2[i] = (prefix2[i - 1] * BASE + value) % MOD2
    power1[i] = power1[i - 1] * BASE % MOD1
    power2[i] = power2[i - 1] * BASE % MOD2

answers = []
position = 2

for _ in range(query_count):
    a, b, c, d = map(int, data[position:position + 4])
    position += 4
    length = b - a + 1

    if length != d - c + 1:
        answers.append("No")
        continue

    hash1_ab = (prefix1[b] - prefix1[a - 1] * power1[length]) % MOD1
    hash1_cd = (prefix1[d] - prefix1[c - 1] * power1[length]) % MOD1
    hash2_ab = (prefix2[b] - prefix2[a - 1] * power2[length]) % MOD2
    hash2_cd = (prefix2[d] - prefix2[c - 1] * power2[length]) % MOD2

    answers.append("Yes" if hash1_ab == hash1_cd and hash2_ab == hash2_cd else "No")

sys.stdout.write("\n".join(answers))