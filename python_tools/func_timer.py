from time import time


def func_timer(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time() - start_time
        print(f'Вы прошли тест за: {end_time:.1f} секунд!')
        return result
    return wrapper
