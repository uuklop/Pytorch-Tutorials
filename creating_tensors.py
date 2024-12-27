import torch


# Creating Tensors

data = torch.empty(2, 3)

data_y = torch.rand(2, 2)

data_z = torch.zeros(2,2)

data_ones = torch.ones(3,3)
print(data_ones)

data_datatype = torch.ones(2,2, dtype=torch.double)
print(data_datatype)
print(data_datatype.size())

data_list = torch.tensor([[2.5,0.1],[3.3,5.5]])
print(data_list)

