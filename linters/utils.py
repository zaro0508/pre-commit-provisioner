from yaml import load, FullLoader
from jinja2 import Template
from pathlib import Path


def load_config(config_path):
    """Produce a Python object (usually dict-like) from the config file at `config_path`

    :param config_path: (str) path to config file, can be absolute or relative to working directory
    :return: Python object representing structure of config file
    """

    # Let YAML handle tags naively
    def default_constructor(loader, tag_suffix, node):
        return tag_suffix + ' ' + node.value
    FullLoader.add_multi_constructor('', default_constructor)

    with open(config_path) as new_file:
        # Load template with blanks for all variables
        template = Template(new_file.read())
        return load(template.render(stack_group_config=''), Loader=FullLoader)


def is_subpath(parent_path: str, child_path: str):
    """Return True if `child_path is a sub-path of `parent_path`

    :param parent_path:
    :param child_path:
    :return:
    """
    return Path(parent_path) in Path(child_path).parents


PATHS = ['config/prod/', 'config/dev/']
SUFFIX = '.yaml'


def get_new_config_paths(all_new_paths):
    """Given a collection of modified paths `all_new_paths`, return those whose paths and file extensions indicate that
    they are Sceptre config files.

    :param all_new_paths:
    :return:
    """
    new_config_paths = []
    for parent_path in PATHS:
        new_config_paths += [path for path in all_new_paths if is_subpath(parent_path, path)]
    return new_config_paths