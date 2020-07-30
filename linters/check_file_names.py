import os
import sys
from .utils import load_config, SUFFIX, get_new_config_paths


def compare_file_and_stack_names():
    all_new_paths = sys.argv[1:]
    new_config_paths = get_new_config_paths(all_new_paths)

    return_code = 0
    for path in new_config_paths:
        config = load_config(path)
        stack_name = config['stack_name']
        filename = os.path.split(path)[-1]
        if (stack_name + SUFFIX) != filename:
            print("Stack name '%s' does not match file name '%s'" % (stack_name, filename))
            return_code = 1
    sys.exit(return_code)
