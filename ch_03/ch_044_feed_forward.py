import torch
import torch.nn as nn

from ch_043_gelu import GELU
from ch_03_ref import print_shape

class FeedForward(nn.Module):
  def __init__(self, cfg):
    super().__init__()
    self.layers = nn.Sequential(
      nn.Linear(cfg["emb_dim"], 4 * cfg["emb_dim"]),
      GELU(),
      nn.Linear(4 * cfg["emb_dim"], cfg["emb_dim"])
    )
    print_shape("Feedforward Input", self.layers[0].weight)

  def forward(self, x):
    return self.layers(x)