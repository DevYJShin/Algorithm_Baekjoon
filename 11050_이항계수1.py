from math import factorial

N, K = list(map(int, input().split()))

print(factorial(N)//(factorial(K) * factorial(N-K)))