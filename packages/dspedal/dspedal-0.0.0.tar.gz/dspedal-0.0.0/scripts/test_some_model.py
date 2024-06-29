import sys
from pathlib import Path

sys.path.append(Path("").absolute().as_posix())

import examples.some_model as some_model

# from ..examples import some_model


def main():
    """"""
    some_model.foo()


if __name__ == "__main__":
    main()
