import torch
import numpy as np

# Initializing Tensors

# 1. Directly from Data
data = [[1, 2], [3, 5]]
x_data = torch.tensor(data)

print(f"CREATING FROM RAW DATA \n tensor data: \n {x_data}\n")
print(f"List: \n {data} \n")

# 2. From numpy Array
np_array = np.array(data)
xp_np = torch.tensor(np_array)
print(f"CREATING FROM NUMPY ARRAYS \n numpy array: \n {np_array}\n")
print(f"xp_np: \n {xp_np} \n")

# 3. Creating from another tensor
x_ones = torch.ones_like(x_data) # retains the properties of x_data
print(f"CREATING FROM OTHER TENSORS \n Ones Tensor: \n {x_ones} \n")

x_rand = torch.rand_like(x_data, dtype=torch.float) # overrides the datatype of x_data
print(f"Random Tensor: \n {x_rand} \n")

# 4. With random or constant values:
# Shape is a tuple of tensor dimensions. in the function below, it determines the dimensionality of the output tensor.
shape = (2, 3)
rand_tensor = torch.rand(shape)
ones_tensor = torch.ones(shape)
zeros_tensor = torch.zeros(shape)

print(f"CREATING FROM RANDOM OR CONSTANT VALUES Random Tensor \n {rand_tensor}\n")
print(f"Ones Tensor: \n {ones_tensor} \n")
print(f"Zeros Tensor: \n {zeros_tensor} \n")

# Attributes of a Tensor
# Shape, datatype, and the device on which they are stored
tensor = torch.randn(3, 4)
print(f"ATTRIBUTES OF TENSOR \nShape of Tensor {tensor.shape}")
print(f"Datatype of Tensor {tensor.dtype}")
print(f"Device tensor is stored on {tensor.device}")