

from datetime import datetime


def logger(func):

    print("line 1")

    def wrapped_func(*args, **kwargs):
        print("line 3")
        if args[0] == 0:
            print("Invalid number")
        return func(*args, **kwargs)

    print("line 2")
    return wrapped_func


# @logger
# def pow2(num):
#     print("line 4")
#     return num ** 2


# @logger
# def is_even(num):
#     return num % 2 == 0


def log_time(fnuc):

    def wrapped_func(*args, **kwargs):
        start_time = datetime.now()
        result = fnuc(*args, **kwargs)
        end_time = datetime.now()
        duration  = end_time - start_time

        print(f"Total time : {duration.seconds // 3600}: {duration.seconds // 60}: {duration.seconds % 60}")

        return result

    return wrapped_func