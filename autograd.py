import torch

# Gradients are important for model optimization

x = torch.randn(3, requires_grad=True)
print(x)

y = x + 2
print(y)

z = y*y*y
print(z)

meanSample = z.mean()
print(meanSample)

# Calculating the gradient
meanSample.backward() #dz/dx
print(x.grad)