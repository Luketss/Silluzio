from pathlib import Path


# List subdirectories:


def list_subdir(path="."):
    p = Path(".")
    print(f"What is p? {type(p)}")
    subdir = [x for x in p.iterdir() if x.is_dir()]
    return subdir


if __name__ == "__main__":
    print(list_subdir())
