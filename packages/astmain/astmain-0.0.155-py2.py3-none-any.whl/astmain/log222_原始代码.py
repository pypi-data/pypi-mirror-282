import builtins

old_print = print

is_debugger = True


def log(is_debugger, *args, **kwargs):
    if is_debugger: old_print(*args, **kwargs)


# 替换内置的 print 函数
#
#
# builtins.print = log
#
# # 使用自定义的 print 函数
# print("Hello, world!")
# print("This is a test.", "Additional message.", sep="-")


if __name__ == '__main__':
    log(is_debugger, 111, 222)

    pass
