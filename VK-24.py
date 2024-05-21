def cache_deco(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result
    return wrapper

def solution(func_map, func_filter, data):
    filtered_data = (x for x in data if func_filter(x))
    mapped_data = (func_map(x) for x in filtered_data)
    for i, x in enumerate(mapped_data):
        if i % 2 == 0:
            yield x

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)