from typing import Any, Dict, Tuple
from functools import wraps


def cache_decorator(func):
    cache: Dict[Any, Any] = {}

    @wraps(func)
    def wrap(*args):
        key: Tuple[Any, ...] = tuple(args)
        result: Any = cache.get(key)

        if result:
            return result

        result: Any = func(*args)
        cache[key] = result
        return result

    return wrap


@cache_decorator
def multiplier(number: int):
    return number * 2
