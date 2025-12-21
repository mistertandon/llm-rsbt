import torch

cuda_available = torch.cuda.is_available()

x = torch.rand(5, 3)

print(x)
print('CUDA Available:', cuda_available)