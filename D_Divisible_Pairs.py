t = int(input())
for _ in range(t):
    res = 0
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n - 1):
        for j in range(i + 1, n):
            if (a[i] + a[j]) % x == 0 and abs(a[i] - a[j]) % y == 0:
                res += 1
            
    print(res)
