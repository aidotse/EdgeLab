from __future__ import print_function
from pathlib import Path
import sys
import torch
import torch.nn.functional as F
import yaml

# local
from util.data_manager import load_data
from util.transformations import np_to_weights, weights_to_np


def train(model, device, train_loader, optimizer, settings):

    print("-- RUNNING TRAINING --", flush=True)

    model.train()

    for epoch in range(1, settings["epochs"] + 1):
        train_loss = 0
        for data, target in train_loader:
            data, target = data.to(device), target.to(device)
            optimizer.zero_grad()
            output = model(data)
            loss = F.nll_loss(output, target)
            train_loss += loss.item()
            loss.backward()
            optimizer.step()
        print(
            "Train Epoch: {} \tLoss: {:.6f}".format(
                epoch,
                # loss.item(),
                train_loss / len(train_loader.dataset),
            )
        )

    print("-- TRAINING COMPLETED --", flush=True)
    return model


if __name__ == "__main__":

    with open("../settings.yaml", "r") as fh:
        try:
            settings = dict(yaml.safe_load(fh))
        except yaml.YAMLError as e:
            raise (e)

    from fedn.utils.pytorchhelper import PytorchHelper
    from models.mnist_pytorch_model import Net

    helper = PytorchHelper()

    use_cuda = torch.cuda.is_available()
    device = torch.device("cuda" if use_cuda else "cpu")

    model = Net().to(device)
    model.load_state_dict(np_to_weights(helper.load_model(sys.argv[1])))

    optimizer = torch.optim.Adam(model.parameters(), lr=0.001, eps=1e-07)
    train_loader = load_data(
        src_data_path=Path("../data/mnist.npz"),
        n_training_samples=settings["training_samples"],
        batch_size=settings["batch_size"],
        use_cuda=use_cuda,
        generated_dataset_path=Path("/tmp/local_dataset"),
        generated_dataset_name="trainset.pickle",
        trainset=True,
    )

    model = train(model, device, train_loader, optimizer, settings)

    helper.save_model(weights_to_np(model.state_dict()), sys.argv[2])
