import builtins,os
import os

old_print = print
def log_is_debugger(is_debugger="True"):
    os.environ['is_debugger'] = is_debugger


def log(*args, **kwargs):
    if os.getenv('is_debugger', 'default_value') == "True": old_print(*args, **kwargs)


# builtins.print = log

# # 使用自定义的 print 函数
# print("Hello, world!")
# print("This is a test.", "Additional message.", sep="-")


if __name__ == '__main__':
    log(111, 222)

    pass
