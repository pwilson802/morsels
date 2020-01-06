from functools import wraps
from dataclasses import dataclass

@dataclass
class Call:
    args: tuple
    kwargs: dict

def record_calls(func):
    @wraps(func)
    def wrapper(*args ,**kwargs):
        wrapper.call_count += 1
        wrapper.calls.append(Call(args, kwargs))
        return func(*args, **kwargs)
    wrapper.call_count = 0
    wrapper.calls = []
    return wrapper

@record_calls
def greet(name):
    return f'hello {name}'