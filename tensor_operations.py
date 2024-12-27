import torch
import numpy as np

# Basic Operations

x = torch.rand(2,2)
y = torch.rand(2,2)
# print(x)
# print(y)
#
# # Addition
# additionOne = x + y
# print(f"First Addition = {additionOne}")
# # or
# addition = torch.add(x,y)
# print(f"Torch method addition = {addition}")
#
# # Inplace addition
# y.add_(x) # any function with a trailing underscore name_ will do an in place operation
# print(f"In-place addition {y}")
#
# #Subtraction
# subtractionOne = x - y
# print(f"\n\nSUBTRACTION\nFirst Subtraction = {subtractionOne}")
# # or
# subtraction = torch.subtract(x,y)
# print(f"Torch method subtraction = {subtraction}")
# x.sub_(y)
# print(f"In-place subtraction {x}")
#
# #Multiplication
# multiplicationOne = x * y
# print(f"\n\nMULTIPLICATION\nFirst multiplication = {multiplicationOne}")
# # or
# multiplication = torch.mul(x,y)
# print(f"Torch method Multiplication = {multiplication}")
# x.mul_(y)
# print(f"In-place multiplication {x}")
#
# #Division
# divisionOne= x / y
# print(f"\n\nDIVISION\nFirst division = {divisionOne}")
# # or
# division = torch.div(x,y)
# print(f"Torch method Division = {division}")
# x.div_(y)
# print(f"In-place Division {x}")

#Slicing Operations
data = torch.rand(5, 3)
print(f"All Data\n{data}")
print(f"First Row: {data[0]}")
print(f"First column: {data[:, 0]}")
print(f"Last column: {data[..., -1]}")
print(f"Last Row: {data[-1:]}")
print(f"All rows for column 0 \n{data[:, 0]}")
print(f"Row number One but all columns \n{data[1, 1]}")

#In-place Operations: Operations that store the result into the operand are called in-place. eg (x_copy(y))


# BRIDGE WITH Numpy
# Tensor to Numpy array
t = torch.ones(5)
print(f"t: {t}")
n = t.numpy()
print(f"n: {n}")

# A change in the tensor reflects in the numpy array.
t.add_(1)
print(f"t: {t}")
print(f"n: {n}")

# Numpy Array to Tensor
n = np.ones(5)
t = torch.from_numpy(n)

np.add(n, 1, out=n)
print(f"t: {t}")
print(f"n: {n}")
