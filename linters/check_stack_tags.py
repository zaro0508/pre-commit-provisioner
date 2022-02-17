import re
import sys
from .utils import load_config, get_new_config_paths


def check_stack_tags():
    """Look in command-line arguments for sceptre config files. Check that each
    file sets `stack_tags`
    """
    all_new_paths = sys.argv[1:]
    new_config_paths = get_new_config_paths(all_new_paths)

    return_code = 0
    for path in new_config_paths:
        config = load_config(path)
        if 'stack_tags' not in config:
            print("- Missing stack_tags key in '%s'" % (path))
            return_code = 1

    sys.exit(return_code)
