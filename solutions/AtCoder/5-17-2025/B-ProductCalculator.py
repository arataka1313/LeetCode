N, K = map(int, input().split())
A = list(map(int, input().split()))

val = 1
for a in A:
    val *= a
    if len(str(val)) > K:
        val = 1

print(val)