MOD = 10**6 + 3

n = int(input())

if n >= MOD:
    print(0)
else:
    remaining_product = 1
    for value in range(n + 1, MOD):
        remaining_product = remaining_product * value % MOD

    factorial = -pow(remaining_product, MOD - 2, MOD) % MOD
    print(factorial)