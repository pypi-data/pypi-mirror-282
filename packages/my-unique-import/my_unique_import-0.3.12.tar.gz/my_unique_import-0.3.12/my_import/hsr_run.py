import os
import subprocess
import argparse
import sys


def get_paramsdict():
    parser = argparse.ArgumentParser(description='Process some text.')
    parser.add_argument("filename", type=str, help="Given a filename")
    parser.add_argument("args", nargs='*', help="Positional arguments")
    parser.add_argument('--kwargs', nargs='*', help='Keyword arguments in the form key=value', default={})

    args = parser.parse_args()

    kwargs = {}
    for kwarg in args.kwargs:
        key, value = kwarg.split('=')
        kwargs[key] = value

    return vars(args)


def run_python(filename, *args, **kwargs):
    if not filename.endswith('.py'):
        filename += '.py'
    abs_filename = os.path.abspath(filename)
    if not os.path.exists(abs_filename):
        print(f"File {abs_filename} does not exist")
        from .file_processing import find_file
        files = find_file(os.getcwd(), filename, False)
        if len(files) == 1:
            abs_filename = os.path.abspath(files[0])
            print(f"Found {abs_filename}")
        else:
            print(f"Found {len(files)} files matching {filename}")
            print(files)
            return
    #     command = [sys.executable, "-c", f"""
    # from my_import.setup_paths import setup_paths
    # setup_paths(verbose=False)
    # with open(r'{abs_filename}') as f:
    #     code = compile(f.read(), r'{abs_filename}', 'exec')
    #     exec(code, {{'__name__': '__main__'}})
    # """]
    # with open(abs_filename, 'r') as file:
    #     code = file.read()

    command = [sys.executable, "-c", f"""
from my_import.setup_paths import setup_paths
setup_paths(verbose=False)
import runpy
runpy.run_path(r'{abs_filename}', run_name='__main__')
"""]

    for arg in args:
        command.append(str(arg))

    for key, value in kwargs.items():
        command.append(f"--{key}")
        command.append(str(value))

    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print("Output:")
        print(result.stdout)
        print("Errors:")
        print(result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Error running {filename}: {e}")
        print("Output:")
        print(e.stdout)
        print("Errors:")
        print(e.stderr)


def main(params=None):
    if params is None:
        params = get_paramsdict()
    run_python(params.get('filename'), *params.get('args'), **params.get('kwargs'))


if __name__ == '__main__':
    main(get_paramsdict())
