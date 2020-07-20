import os
import sys
from .utils import load_config, is_subpath

PATHS = ['config/']
SUFFIX = '.yaml'


def compare_file_and_stack_names():
    print("Arguments:")  # FIXME: this line is for debugging purposes
    print(sys.argv)  # FIXME: this line too
    all_new_paths = sys.argv[1:]

    new_config_paths = []
    for parent_path in PATHS:
        new_config_paths = [path for path in all_new_paths if is_subpath(parent_path, path)]

    return_code = 0
    for path in new_config_paths:
        config = load_config(path)
        stack_name = config['stack_name']
        filename = os.path.split(path)[-1]
        if (stack_name + SUFFIX) != filename:
            print("Stack name '%s' does not match file name '%s'" % (stack_name, filename))
            return_code = 1
    sys.exit(return_code)
