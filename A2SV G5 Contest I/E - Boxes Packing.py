n = int(input())
m = {}
mc = 0

input_string = input()
input_list = [int(char) for char in input_string.split()]

for i in range(n):
    x = input_list[i]
    if x in m:
        m[x] += 1
    else:
        m[x] = 1

    mc = max(mc, m[x])

print(mc)