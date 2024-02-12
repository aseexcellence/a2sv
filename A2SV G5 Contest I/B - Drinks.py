n = int(input())
percentages = list(map(int, input().split()))

total_percentage = sum(percentages)
cocktail_percentage = total_percentage / n

print("{:.9f}".format(cocktail_percentage))


