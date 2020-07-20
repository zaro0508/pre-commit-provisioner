import os
import sys
from .utils import load_config, list_new_configs

PATHS = ['config/']
SUFFIX = '.yaml'


def compare_file_and_stack_names():
    print("Arguments:")  # FIXME: this line is for debugging purposes
    print(sys.argv)  # FIXME: this line too
    new_file_paths = list_new_configs(PATHS)
    return_code = 0
    for path in new_file_paths:
        config = load_config(path)
        stack_name = config['stack_name']
        filename = os.path.split(path)[-1]
        if (stack_name + SUFFIX) != filename:
            print("Stack name '%s' does not match file name '%s'" % (stack_name, filename))
            return_code = 1
    sys.exit(return_code)
