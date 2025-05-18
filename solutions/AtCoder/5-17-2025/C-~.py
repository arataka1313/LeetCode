def is_tilde4(a, b, c, d):
    pattern1 = a < b > c < d
    pattern2 = a > b < c > d
    return pattern1 or pattern2

count = 0
N = int(input())
P = list(map(int, input().split()))

for i in range(N - 3):
    if is_tilde4(P[i], P[i+1], P[i+2], P[i+3]):
        count += 1

print(count)
