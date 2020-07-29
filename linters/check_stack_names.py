import re
import sys
from .utils import load_config, get_new_config_paths


STACK_NAME_DOCUMENTATION = """A stack name can contain only alphanumeric characters (case-sensitive) and hyphens. It \
must start with an alphabetic character and can't be longer than 128 characters.
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-using-console-create-stack-parameters.html
"""
STACK_NAME_PATTERN = re.compile("^[a-zA-Z][a-zA-Z0-9\-]{0,127}$")


def check_stack_names():
    """Look in command-line arguments for cloudformation config files. Check that the `stack_name` value for each one
    matches the requirements outlined in `STACK_NAME_DOCUMENTATION`.
    """
    all_new_paths = sys.argv[1:]
    new_config_paths = get_new_config_paths(all_new_paths)

    return_code = 0
    for path in new_config_paths:
        config = load_config(path)
        stack_name = config['stack_name']
        if not re.match(STACK_NAME_PATTERN, stack_name):
            print("- '%s' is an invalid stack name (in '%s')" % (stack_name, path))
            return_code = 1

    if return_code:
        print(STACK_NAME_DOCUMENTATION)

    sys.exit(return_code)

