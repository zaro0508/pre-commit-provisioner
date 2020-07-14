import os
import utils


def compare_file_and_stack_name(paths='config/', suffix='.yaml'):
    new_file_paths = utils.list_new_configs(paths)
    for path in new_file_paths:
        config = utils.load_config(path)
        stack_name = config['stack_name']
        filename = os.path.split(path)[-1]
        assert (stack_name + suffix) == filename,\
            "Stack name '%s' does not match file name '%s'" % (stack_name, filename)
