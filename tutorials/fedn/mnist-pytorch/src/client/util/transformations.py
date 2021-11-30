import collections
import torch


def weights_to_np(weights: collections.OrderedDict) -> collections.OrderedDict:
    weights_np = collections.OrderedDict()
    for w in weights:
        weights_np[w] = weights[w].cpu().detach().numpy()
    return weights_np


def np_to_weights(weights_np: collections.OrderedDict) -> collections.OrderedDict:
    weights = collections.OrderedDict()
    for w in weights_np:
        weights[w] = torch.tensor(weights_np[w])
    return weights
