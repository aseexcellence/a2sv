if __name__ == '__main__':
    n = int(input())
    # change map type to list type to iterate
    arr = list(map(int, input().split()))
    
    # logic to find the largest number in the list
    max = arr[0]
    for a in arr:
        if (max <= a):
            max = a
    
    '''logic to remove the largest number so the
    remaining largest number would be the runner-up score'''
    while (max in arr):
        arr.remove(max)
    
    max = arr[0]
    for result in arr:
        if (max < result):
            max = result
    print(max)
