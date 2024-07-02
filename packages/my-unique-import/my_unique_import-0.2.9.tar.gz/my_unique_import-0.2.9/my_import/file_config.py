import os
import sys

import inspect
import os
import pkgutil


def find_top_level_package():
    current_frame = inspect.currentframe()
    file_path = inspect.getfile(current_frame)
    print(file_path)
    current_dir = os.path.dirname(os.path.abspath(file_path))
    below_dir = current_dir
    while current_dir:
        if '__init__.py' in os.listdir(current_dir):
            parent_dir = os.path.dirname(current_dir)
            if parent_dir == current_dir:  # 根目录
                break
            below_dir = current_dir
            current_dir = parent_dir
        else:
            break
    return below_dir

def main():
    print(find_top_level_package())


if __name__ == '__main__':
    main()
