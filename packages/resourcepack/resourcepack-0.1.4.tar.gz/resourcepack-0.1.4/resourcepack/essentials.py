import git
from pathlib import Path


def get_project_root():
    """
    Get the root directory of the project.

    :return: The root directory of the project.
    """
    return Path(git.Repo('.', search_parent_directories=True).working_tree_dir)