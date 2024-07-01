import builtins

old_print = print

is_debugger = False


def log(*args, **kwargs):
    old_print(*args, **kwargs)


# 替换内置的 print 函数


builtins.print = log

# 使用自定义的 print 函数
print("Hello, world!")
print("This is a test.", "Additional message.", sep="-")
