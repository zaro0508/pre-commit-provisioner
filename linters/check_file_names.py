import os
from .utils import load_config, list_new_configs

PATHS = ['config/']
SUFFIX = '.yaml'


def compare_file_and_stack_names():
    new_file_paths = list_new_configs(PATHS)
    for path in new_file_paths:
        config = load_config(path)
        stack_name = config['stack_name']
        filename = os.path.split(path)[-1]
        assert (stack_name + SUFFIX) == filename,\
            "Stack name '%s' does not match file name '%s'" % (stack_name, filename)
