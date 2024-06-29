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