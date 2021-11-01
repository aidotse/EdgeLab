from datetime import datetime
from pathlib import Path
import torch

from fedn.utils.pytorchhelper import PytorchHelper
from src.client.models.mnist_pytorch_model import Net
from src.client.util.transformations import weights_to_np


if __name__ == "__main__":
    package_path = Path("package")
    if not package_path.is_dir():
        package_path.mkdir()

    use_cuda = torch.cuda.is_available()
    device = torch.device("cuda" if use_cuda else "cpu")
    model = Net().to(device)

    outfile_name = "package/initial_model.npz"

    # Add time stamp
    # date = datetime.now().strftime("%Y%m%d%I%M%S")
    # outfile_name = f"package/initial_model_{date}.npz"

    helper = PytorchHelper()
    helper.save_model(weights_to_np(model.state_dict()), outfile_name)

    print("done")
