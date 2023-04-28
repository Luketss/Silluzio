from os import listdir, getcwd, mkdir, remove, rename, chdir
from os.path import isfile, join, isdir


def list_all_files_in_dir(dir_path: str) -> list:
    files = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]
    return files


def list_all_dir_in_dir(dir_path: str) -> list:
    dir = [d for d in listdir(dir_path) if isdir(join(dir_path, d))]
    return dir


def create_new_dir(dir_name: str, parent_dir=None) -> str:
    if parent_dir is None:
        parent_dir = getcwd()
    path = join(parent_dir, dir_name)
    mkdir(path)
    return f"Directory created at {path}"


def delete_dir(dir_name: str, parent_dir=None) -> str:
    if parent_dir is None:
        parent_dir = getcwd()
    path = join(parent_dir, dir_name)
    remove(path)
    return f"Directory deleted at {path}"


def rename_dir(new_name: str, old_name: str, working_directory: str) -> str:
    chdir(working_directory)

    rename(old_name, new_name)
    return f"renamed from {old_name} to {new_name}"


def moves_file_to_folder():
    pass


def copy_file():
    pass


def check_if_a_dir_exist():
    pass


def change_working_dir():
    pass


def print_files_and_dirs_recursively_in_root():
    pass


if __name__ == "__main__":
    pass
