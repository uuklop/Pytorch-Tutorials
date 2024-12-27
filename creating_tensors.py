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