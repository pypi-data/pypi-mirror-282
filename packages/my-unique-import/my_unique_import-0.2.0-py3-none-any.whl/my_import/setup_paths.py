import functools
import os
import sys
import inspect


def setup_paths():
    caller_file = inspect.stack()[-1].filename
    caller_dir = os.path.dirname(os.path.abspath(caller_file))
    project_root = os.path.abspath(os.path.join(caller_dir, '..'))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)

    print(caller_file)


def log_call_position(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        stack = inspect.stack()

        calling_frame = stack[1]
        filename = calling_frame.filename
        lineno = calling_frame.lineno
        sys.stdout.write(f"函数 {func.__name__} 被调用于: 文件名={filename}, 行号={lineno}\n")

        return func(*args, **kwargs)

    return wrapper


def find_print():
    import builtins
    original_print = builtins.print
    builtins.print = log_call_position(original_print)