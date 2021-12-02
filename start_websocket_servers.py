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

#print(Path(__file__).resolve()[-1])
#FILE_PATH = Path(__file__).resolve().parents[4].joinpath("run_websocket_server.py")
FILE_PATH = Path(__file__).resolve().parents[0].joinpath("run_websocket_server.py")
print(FILE_PATH)

call_alice = [
    python,
    FILE_PATH,
    "--port",
    "8777",
    "--id",
    "alice",
    "--host",
    "0.0.0.0",
    "--notebook",
    "mnist-parallel",
]

call_bob = [
    python,
    FILE_PATH,
    "--port",
    "8778",
    "--id",
    "bob",
    "--host",
    "0.0.0.0",
    "--notebook",
    "mnist-parallel",
]

print("Starting server for alice")
process_alice = subprocess.Popen(call_alice)

print("Starting server for Bob")
process_bob = subprocess.Popen(call_bob)

def signal_handler(sig, frame):
    print("You pressed Ctrl+C!")
    for p in [process_alice, process_bob, process_charlie, process_testing]:
        p.terminate()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

signal.pause()