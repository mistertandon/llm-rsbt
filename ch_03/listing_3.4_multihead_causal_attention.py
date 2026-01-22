import torch
import torch.nn as nn
from ch_03_353_compact_causal_attention import CausalAttention


class MultiheadAttentionWrapper(nn.Module):
    def __init__(self, num_heads, d_in, d_out, qkv_bias, context_length, dropout):
        super().__init__()
        self.num_heads = num_heads
        self.heads = nn.ModuleList(
            [
                CausalAttention(d_in, d_out, context_length, dropout, qkv_bias)
                for _ in range(num_heads)
            ]
        )

    def forward(self, x):
        return torch.cat([head(x) for head in self.heads], dim=-1)


inputs = torch.tensor(
    [
        [0.43, 0.15, 0.89],  # Your     (x^1)
        [0.55, 0.87, 0.66],  # journey  (x^2)
        [0.57, 0.85, 0.64],  # starts   (x^3)
        [0.22, 0.58, 0.33],  # with     (x^4)
        [0.77, 0.25, 0.10],  # one      (x^5)
        [0.05, 0.80, 0.55],  # step     (x^6)
    ]
)

batch = torch.stack([inputs, inputs], dim=0)
num_heads = batch.shape[0]
d_in = batch.shape[2]
context_length = batch.shape[1]
print(batch.shape)
print(batch)

causal_attention = MultiheadAttentionWrapper(
    num_heads=2,
    d_in=d_in,
    d_out=2,
    context_length=context_length,
    dropout=0.1,
    qkv_bias=False,
)

context_vectors = causal_attention(batch)
print("Context Vectors: ", context_vectors)
