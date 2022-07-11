from functools import lru_cache


@lru_cache
def multiplier(number: int):
    return number * 2
