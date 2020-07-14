from git import Repo, DiffIndex, Diff
from yaml import load, FullLoader


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


def list_new_configs(paths, suffix='.yaml'):
    """Use Git to list new (in the staging area) files ending in '.yaml' in `paths`

    :param paths: (list) paths in which to check for config files
    :param suffix: (str) filename suffix that config files are expected to have
    :return: list of relative paths for config files
    """
    repo = Repo()

    # Get diff of staging area and working tree (i.e. files about to committed)
    diff_index: DiffIndex = repo.head.commit.diff(paths=paths)

    filepaths = []
    diff: Diff
    for diff in diff_index:
        # If a file has been added or modified, the filename ends with the correct extension:
        if diff.change_type in {'A', 'M'} and diff.a_path.endswith(suffix):
            filepaths.append(diff.a_path)
    return filepaths
