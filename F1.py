import sys

MOD = 10**9 + 9

data = list(map(int, sys.stdin.buffer.read().split()))
test_count = data[0]

answers = [str(pow(a, MOD - 2, MOD)) for a in data[1:test_count + 1]]
sys.stdout.write("\n".join(answers))