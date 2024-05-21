def repeat_deco(n=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n-1):
                func(*args, **kwargs)
            return func(*args, **kwargs)
        return wrapper
    return decorator

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)