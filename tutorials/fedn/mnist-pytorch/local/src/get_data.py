#!/usr/bin/python3

import torchvision
from pathlib import Path
import shutil
import sys


def get_data(out_path: Path = Path().absolute().joinpath("data")):
    if out_path.exists():
        try:
            shutil.rmtree(out_path)
        except OSError as e:
            print(f"Error: {out_path} : {e.strerror}")
            sys.exit(1)
    # Make dir if necessary
    if not out_path.exists():
        out_path.mkdir(parents=True, exist_ok=True)

    train_path = out_path.joinpath("train")
    test_path = out_path.joinpath("test")

    # Download data
    torchvision.datasets.MNIST(
        root=train_path,
        transform=torchvision.transforms.ToTensor,
        train=True,
        download=True,
    )
    torchvision.datasets.MNIST(
        root=test_path,
        transform=torchvision.transforms.ToTensor,
        train=False,
        download=True,
    )


if __name__ == "__main__":
    get_data()
