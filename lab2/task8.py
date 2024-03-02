import time


def retry(max_tries, delta, on_exceptions):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(max_tries):
                try:
                    result = func(*args, **kwargs)
                    return result
                except on_exceptions as e:
                    if i < max_tries - 1:
                        print(f"Попробуем через {delta} секунд...")
                        time.sleep(delta)
                    else:
                        raise e

        return wrapper

    return decorator


@retry(max_tries=5, delta=1, on_exceptions=Exception)
def test(data, n):
    for i in data:
        if i == n:
            return i
        else:
            data.remove(i)
            raise Exception('Упси, не то число')


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(test(data=data, n=10))
