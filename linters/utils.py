from yaml import load, FullLoader
from pathlib import Path


# Let YAML handle tags naively
def default_constructor(loader, tag_suffix, node):
    return tag_suffix + ' ' + node.value
FullLoader.add_multi_constructor('', default_constructor)


def load_config(config_path):
    """Produce a Python object (usually dict-like) from the config file at `config_path`

    :param config_path: (str) path to config file, can be absolute or relative to working directory
    :return: Python object representing structure of config file
    """
    with open(config_path) as new_file:
        return load(new_file, Loader=FullLoader)


def is_subpath(parent_path: str, child_path: str):
    """Return True if `child_path is a sub-path of `parent_path`

    :param parent_path:
    :param child_path:
    :return:
    """
    return Path(parent_path) in Path(child_path).parents

