import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    i, j = 1, n
    ans, w1, x1, w2, x2 = 0, 0, 0, 0, 0

    while i <= j:
        if w1 < w2:
            x1 += 1
            w1 += a[i]
            i += 1
        if w2 < w1:
            x2 += 1
            w2 += a[j]
            j -= 1
        if w1 == w2:
            if x1 + x2 > ans:
                ans = x1 + x2
            w2 += a[j]
            j -= 1
            x2 += 1

    print(ans)
