import numpy as np
from pathlib import Path
import pickle
import torch
from torch.utils.data import Subset
from torch.utils.data import TensorDataset, DataLoader


def load_data(
    src_data_path: Path,
    n_training_samples: int,
    batch_size: int,
    use_cuda: bool,
    generated_dataset_path: Path,
    generated_dataset_name: str,
    trainset: bool = True,
):
    data_path = generated_dataset_path.joinpath(generated_dataset_name)

    # We are caching the partition in the container home dir so that
    # the same training subset is used for each iteration for a client.
    try:
        with open(data_path, "rb") as fh:
            dataset = pickle.loads(fh.read())
        print("load local dataset")

    except:
        dataset = read_data(
            trainset=trainset,
            nr_examples=n_training_samples,
            data_path=src_data_path,
        )
        print("sample new local trainset")

        try:
            if not generated_dataset_path.is_dir():
                generated_dataset_path.mkdir(parents=True, exist_ok=True)

            with open(data_path, "wb") as fh:
                fh.write(pickle.dumps(dataset))

        except:
            pass

    dataset_kwargs = {"batch_size": batch_size, "shuffle": True}
    if use_cuda:
        # cuda_kwargs = {"num_workers": 1, "pin_memory": True, "shuffle": True}
        cuda_kwargs = {"pin_memory": True}
        dataset_kwargs.update(cuda_kwargs)

    return DataLoader(dataset, **dataset_kwargs)


def read_data(trainset=True, nr_examples=1000, data_path="data/mnist.npz"):
    """Helper function to read and preprocess data for training with Keras."""

    pack = np.load(data_path)

    if trainset:
        X = pack["x_train"]
        y = pack["y_train"]
    else:
        X = pack["x_test"]
        y = pack["y_test"]

    X = X.astype("float32")
    y = y.astype("int64")

    X = np.expand_dims(X, 1)
    X /= 255
    tensor_x = torch.Tensor(X)  # transform to torch tensor
    tensor_y = torch.from_numpy(y)
    dataset = TensorDataset(tensor_x, tensor_y)  # create traindatset
    sample = np.random.choice(np.arange(len(dataset)), nr_examples, replace=False)
    dataset = Subset(dataset=dataset, indices=sample)

    return dataset
