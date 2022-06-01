#!/usr/bin/python3

import torchvision
import torch
from pathlib import Path
import shutil
import sys


def splitset(dataset, parts):
    n = dataset.shape[0]
    local_n = n // parts
    result = list()
    for i in range(parts):
        result.append(dataset[i * local_n : (i + 1) * local_n])
    return result


def split(out_path: Path = Path().absolute().joinpath("data"), n_splits: int = 2):
    clients_path = out_path.joinpath("clients")
    if clients_path.exists():
        try:
            shutil.rmtree(clients_path)
        except OSError as e:
            print(f"Error: {out_path} : {e.strerror}")
            sys.exit(1)
    # Make dir
    clients_path.mkdir(parents=True, exist_ok=True)

    train_path = out_path.joinpath("train")
    test_path = out_path.joinpath("test")

    # Load and convert to dict
    train_data = torchvision.datasets.MNIST(
        root=train_path, transform=torchvision.transforms.ToTensor, train=True
    )
    test_data = torchvision.datasets.MNIST(
        root=test_path, transform=torchvision.transforms.ToTensor, train=False
    )
    data = {
        "x_train": splitset(train_data.data, n_splits),
        "y_train": splitset(train_data.targets, n_splits),
        "x_test": splitset(test_data.data, n_splits),
        "y_test": splitset(test_data.targets, n_splits),
    }

    # Make splits
    for i in range(n_splits):
        sub_path = clients_path.joinpath(str(i + 1))
        if not sub_path.exists():
            sub_path.mkdir(parents=True, exist_ok=True)

        torch.save(
            {
                "x_train": data["x_train"][i],
                "y_train": data["y_train"][i],
                "x_test": data["x_test"][i],
                "y_test": data["y_test"][i],
            },
            sub_path.joinpath("mnist.pt"),
        )


if __name__ == "__main__":
    split()
