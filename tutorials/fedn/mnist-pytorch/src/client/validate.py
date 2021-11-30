import json
from pathlib import Path
import sys
import torch
import torch.nn.functional as F
import yaml


from fedn.utils.pytorchhelper import PytorchHelper
from models.mnist_pytorch_model import Net
from util.transformations import np_to_weights
from util.data_manager import load_data


def validate(
    model: torch.nn.Module,
    device: torch.device,
    train_loader: torch.utils.data.dataloader.DataLoader,
    test_loader: torch.utils.data.dataloader.DataLoader,
    settings: dict,
) -> dict:
    print("-- RUNNING VALIDATION --", flush=True)
    # The data, split between train and test sets. We are caching the partition in
    # the container home dir so that the same data subset is used for
    # each iteration.

    def evaluate(
        model: torch.nn.Module,
        device: torch.device,
        data_loader: torch.utils.data.dataloader.DataLoader,
    ):
        model.eval()
        test_loss = 0
        correct = 0
        with torch.no_grad():
            for data, target in data_loader:
                data, target = data.to(device), target.to(device)
                output = model(data)
                test_loss += F.nll_loss(
                    output, target, reduction="sum"
                ).item()  # sum up batch loss
                pred = output.argmax(
                    dim=1, keepdim=True
                )  # get the index of the max log-probability
                correct += pred.eq(target.view_as(pred)).sum().item()

        test_loss /= len(data_loader.dataset)
        test_acc = 100.0 * correct / len(data_loader.dataset)

        return float(test_loss), float(test_acc)

    try:
        training_loss, training_acc = evaluate(model, device, train_loader)
        test_loss, test_acc = evaluate(model, device, test_loader)

    except Exception as e:
        print("failed to validate the model {}".format(e), flush=True)
        raise

    report = {
        "classification_report": "unevaluated",
        "training_loss": training_loss,
        "training_accuracy": training_acc,
        "test_loss": test_loss,
        "test_accuracy": test_acc,
    }

    print("-- VALIDATION COMPLETE! --", flush=True)
    return report


if __name__ == "__main__":

    with open("../settings.yaml", "r") as fh:
        try:
            settings = dict(yaml.safe_load(fh))
        except yaml.YAMLError as e:
            raise (e)

    helper = PytorchHelper()

    use_cuda = torch.cuda.is_available()
    device = torch.device("cuda" if use_cuda else "cpu")

    model = Net().to(device)
    model.load_state_dict(np_to_weights(helper.load_model(sys.argv[1])))

    train_loader = load_data(
        src_data_path=Path("../data/mnist.npz"),
        n_training_samples=settings["training_samples"],
        batch_size=settings["batch_size"],
        use_cuda=use_cuda,
        generated_dataset_path=Path("/tmp/local_dataset"),
        generated_dataset_name="trainset.pickle",
        trainset=True,
    )

    test_loader = load_data(
        src_data_path=Path("../data/mnist.npz"),
        n_training_samples=settings["test_samples"],
        batch_size=settings["batch_size"],
        use_cuda=use_cuda,
        generated_dataset_path=Path("/tmp/local_dataset"),
        generated_dataset_name="testset.pickle",
        trainset=False,
    )

    report = validate(model, device, train_loader, test_loader, settings)

    print(
        "Training: Acc: {} \tLoss: {:.6f}".format(
            report["training_accuracy"],
            report["training_loss"],
        )
    )
    print(
        "Test: Acc: {} \tLoss: {:.6f}".format(
            report["test_accuracy"],
            report["test_loss"],
        )
    )

    with open(sys.argv[2], "w") as fh:
        fh.write(json.dumps(report))
