t = int(input())

for _ in range(t):
    n, x1, y1, x2, y2 = map(int, input().split())
    start = min(min(x1, n + 1 - x1), min(y1, n + 1 - y1))
    finish = min(min(x2, n + 1 - x2), min(y2, n + 1 - y2))
    diff = abs(start - finish)
    print(diff)
