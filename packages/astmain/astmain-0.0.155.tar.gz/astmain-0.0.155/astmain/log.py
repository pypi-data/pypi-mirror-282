import builtins, os
import os


def log_is_debugger(is_debugger="True"):
    os.environ['is_debugger'] = is_debugger


def log(*args, **kwargs):
    if os.getenv('is_debugger', 'True') == "True": print(*args, **kwargs)


if __name__ == '__main__':
    log(111, 222)

    pass
