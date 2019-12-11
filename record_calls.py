def record_calls(func):
    def wrapper(*args):
        try:
            func.call_count += 1
        except AttributeError:
            func.call_count = 1
        print(f'Running {func.__name__}')
        print(func.call_count)
        return func(*args)
    return wrapper

@record_calls
def greet(name):
    return f'hello {name}'