MOD = 10**9 + 7

a, b, c, d = map(int, input().split())

numerator = (a * d + b * c) % MOD
denominator = (b * d) % MOD

print(numerator * pow(denominator, MOD - 2, MOD) % MOD)