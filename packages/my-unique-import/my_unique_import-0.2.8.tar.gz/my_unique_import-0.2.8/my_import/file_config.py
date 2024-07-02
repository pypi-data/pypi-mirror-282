import os
import sys


def main():
    print(os.getcwd())
    print(sys.executable)
    print(sys.gettrace())
    print(__file__)


if __name__ == '__main__':
    main()
