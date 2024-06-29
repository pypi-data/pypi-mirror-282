"""Test rounding algorithms."""

import numpy as np


def bytesize(x: int):
    """Round up to nearest byte size."""


def stdintsize(n: int):
    """Round up to nearest stdint size"""
    base = np.ceil(np.log2(n)) if n > 8 else 3
    return int(2**base)


vmin_stdint = np.vectorize(stdintsize)


def test_stdintsize():
    """"""

    x = np.arange(1, 64)
    for xx, bb in zip(x, vmin_stdint(x)):
        print(f"X: {xx}, Base: {bb}")


if __name__ == "__main__":
    test_stdintsize()
