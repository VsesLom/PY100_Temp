def header_footer(fn):  # написать декоратор
    def wrapper(*args, **kwargs):
        print('=' * 8)
        result = fn(*args, **kwargs)
        print('=' * 8)
        return result
    return wrapper


@header_footer
def my_func():
    print("Hello World")


if __name__ == "__main__":
    my_func()
