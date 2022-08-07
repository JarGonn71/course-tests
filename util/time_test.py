import time


def sleep_dec(function):
    start = time.perf_counter()

    def wrapper(*args):
        return function(*args)

    end = time.perf_counter()
    print(f"test: {end - start} seconds")
    return wrapper
