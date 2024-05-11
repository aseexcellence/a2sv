for _ in range(int(input())):
    k, q = map(int, input().split())
    a = list(map(int, input().split()))

    n_list = list(map(int, input().split()))
    for n in n_list:
        print(min(a[0] - 1, n), end=' ')
    print()
    
        

