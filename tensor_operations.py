import torch
import numpy as np

x = torch.rand(2,2)
y = torch.rand(2,2)
print(x)
print(y)

# Addition
additionOne = x + y
print(f"First Addition = {additionOne}")
# or
addition = torch.add(x,y)
print(f"Torch method addition = {addition}")

# Inplace addition
y.add_(x) # any function with a trailing underscore name_ will do an in place operation
print(f"In-place addition {y}")