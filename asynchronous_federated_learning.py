import asyncio






import subprocess

from torchvision import datasets
from torchvision import transforms
from pathlib import Path

import signal
import sys

# Downloads MNIST dataset
mnist_trainset = datasets.MNIST(
    root="./data",
    train=True,
    download=True,
    transform=transforms.Compose(
        [transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))]
    ),
)

python = Path(sys.executable).name

FILE_PATH = Path(__file__).resolve().parents[0].joinpath("run_websocket_server.py")

call_testing = [
    python,
    FILE_PATH,
    "--port",
    "8780",
    "--id",
    "testing",
    "--testing",
    "--host",
    "0.0.0.0",
    "--notebook",
    "mnist-parallel",
]

print("Starting server for Testing")
#process_testing = subprocess.Popen(call_testing)





async def main():
    import inspect

    import sys

    import syft as sy
    from syft.workers.websocket_client import WebsocketClientWorker
    from syft.frameworks.torch.fl import utils

    import torch
    from torchvision import datasets, transforms
    import numpy as np

    import run_websocket_client as rwc

    # Hook torch
    hook = sy.TorchHook(torch)

    # Arguments
    args = rwc.define_and_get_arguments(args=[])
    use_cuda = args.cuda and torch.cuda.is_available()
    torch.manual_seed(args.seed)
    device = torch.device("cuda" if use_cuda else "cpu")
    print(args)
    args.batch_size = 128
    args.save_model = True

    # Configure logging
    import logging

    logger = logging.getLogger("run_websocket_client")

    if not len(logger.handlers):
        FORMAT = "%(asctime)s - %(message)s"
        DATE_FMT = "%H:%M:%S"
        formatter = logging.Formatter(FORMAT, DATE_FMT)
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.propagate = False
        LOG_LEVEL = logging.DEBUG
        logger.setLevel(LOG_LEVEL)

    kwargs_websocket = {"hook": hook, "verbose": args.verbose}
    alice = WebsocketClientWorker(id="alice", port=8777, host="172.25.17.169", **kwargs_websocket)
    bob = WebsocketClientWorker(id="bob", port=8778, host="172.25.17.171", **kwargs_websocket)
    #testing = WebsocketClientWorker(id="testing", port=8780, host="0.0.0.0", **kwargs_websocket)

    worker_instances = [alice, bob]

    print(inspect.getsource(rwc.Net))

    model = rwc.Net().to(device)
    print(model)

    traced_model = torch.jit.trace(model, torch.zeros([1, 1, 28, 28], dtype=torch.float))

    print("Federate_after_n_batches: " + str(args.federate_after_n_batches))
    print("Batch size: " + str(args.batch_size))
    print("Initial learning rate: " + str(args.lr))

    learning_rate  = args.lr
    device = "cpu"  #torch.device("cpu")
    traced_model = torch.jit.trace(model, torch.zeros([1, 1, 28, 28], dtype=torch.float))

    for curr_round in range(1, args.training_rounds + 1):
        logger.info("Training round %s/%s", curr_round, args.training_rounds)

        results = await asyncio.gather(
            *[
                rwc.fit_model_on_worker(
                    worker=worker,
                    traced_model=traced_model,
                    batch_size=args.batch_size,
                    curr_round=curr_round,
                    max_nr_batches=args.federate_after_n_batches,
                    lr=learning_rate,
                )
                for worker in worker_instances
            ]
        )
        models = {}
        loss_values = {}

        #test_models = curr_round % 10 == 1 or curr_round == args.training_rounds
        #if test_models:
        #    logger.info("Evaluating models")
        #    np.set_printoptions(formatter={"float": "{: .0f}".format})
        #    for worker_id, worker_model, _ in results:
        #        rwc.evaluate_model_on_worker(
        #            model_identifier="Model update " + worker_id,
        #            worker=testing,
        #            dataset_key="mnist_testing",
        #            model=worker_model,
        #            nr_bins=10,
        #            batch_size=128,
        #            print_target_hist=False,
        #            device=device
        #        )

        # Federate models (note that this will also change the model in models[0]
        for worker_id, worker_model, worker_loss in results:
            if worker_model is not None:
                models[worker_id] = worker_model
                loss_values[worker_id] = worker_loss

        traced_model = utils.federated_avg(models)

        #if test_models:
        #    rwc.evaluate_model_on_worker(
        #        model_identifier="Federated model",
        #        worker=testing,
        #        dataset_key="mnist_testing",
        #        model=traced_model,
        #        nr_bins=10,
        #        batch_size=128,
        #        print_target_hist=False,
        #        device=device
        #    )

        # decay learning rate
        learning_rate = max(0.98 * learning_rate, args.lr * 0.01)

    if args.save_model:
        torch.save(model.state_dict(), "mnist_cnn.pt")

asyncio.get_event_loop().run_until_complete(main())