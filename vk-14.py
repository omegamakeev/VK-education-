start, end, step = map(int, input().split())
result = [x**2 if x%2 else -x for x in range(start, end, step)]
print(*result, sep='\n')