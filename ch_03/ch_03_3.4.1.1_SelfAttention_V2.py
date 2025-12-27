import torch
import torch.nn as nn

""" Self-Attention V2 Implementation
How to run:
python ch_03/ch_03_3.4.1.1_SelfAttention_V2.py
"""
class SelfAttention_V2(nn.Module):

    def __init__(self, d_in, d_out, qkv_bias=False):
        super().__init__()
        torch.manual_seed(123)
        self.W_query = nn.Linear(d_in, d_out, bias=qkv_bias)
        self.W_key = nn.Linear(d_in, d_out, bias=qkv_bias)
        self.W_value = nn.Linear(d_in, d_out, bias=qkv_bias)
    
    def forward(self, x):
        queries = self.W_query(x)
        keys = self.W_key(x)
        values = self.W_value(x)

        d_k = keys.shape[-1]
        attention_scores = torch.matmul(queries, keys.T)
        attention_weights = torch.softmax(attention_scores/torch.sqrt(torch.tensor(d_k, dtype = torch.float32)), dim=-1)
        context_vectors = torch.matmul(attention_weights, values)

        return context_vectors


inputs = torch.tensor(
  [[0.43, 0.15, 0.89], # Your     (x^1)
   [0.55, 0.87, 0.66], # journey  (x^2)
   [0.57, 0.85, 0.64], # starts   (x^3)
   [0.22, 0.58, 0.33], # with     (x^4)
   [0.77, 0.25, 0.10], # one      (x^5)
   [0.05, 0.80, 0.55]] # step     (x^6)
)

d_in = inputs.shape[-1]
d_out = 2

sa_v2 = SelfAttention_V2(d_in, d_out)
context_vectors = sa_v2(inputs)

print("Context Vectore: ", context_vectors)
