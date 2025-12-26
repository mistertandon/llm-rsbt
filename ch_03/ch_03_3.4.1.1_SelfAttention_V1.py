import torch
import torch.nn as nn

class SelfAttention_V1(nn.Module):

    def __init__(self, d_in, d_out):
        super().__init__()
        torch.manual_seed(123)
        self.W_query = nn.Parameter(torch.randn(d_in, d_out))
        self.W_key = nn.Parameter(torch.randn(d_in, d_out))
        self.W_value = nn.Parameter(torch.randn(d_in, d_out))
    
    def forward(self, x):
        queries = torch.matmul(x, self.W_query)
        keys = torch.matmul(x, self.W_key)
        values = torch.matmul(x, self.W_value)

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

sa_v1 = SelfAttention_V1(d_in, d_out)
context_vectors = sa_v1(inputs)

print("Context Vectore: ", context_vectors)
