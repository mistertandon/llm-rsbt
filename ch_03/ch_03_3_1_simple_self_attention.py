import torch

def naive_softmax(x):
    normalized = torch.exp(x)/torch.exp(x).sum(dim=0)
    return normalized