t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    for i in range(n):
        if s[i] > i + 1:
            print(-1)
            break
        elif s[i] == s[-1]:
            print(*range(n, 0, -1))
            break
        elif s[i] <= i + 1:
            print(*[n] + list(range(1, n)))
            break
