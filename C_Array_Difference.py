t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort(reverse=True)
    c = [0] * n
    _sum = 0
    for i in range(n):
        c[i] = b[m - n + i]
        _sum += abs(c[i] - a[i])
    res = 0
    for k in range(n + 1):
        res = max(res, _sum)
        if k < n:
            _sum -= abs(c[k] - a[k])
            c[k] = b[k]
            _sum += abs(c[k] - a[k])
    print(res)

