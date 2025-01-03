import torch
from triton.language import dtype

# Gradients are important for model optimization

x = torch.randn(3, requires_grad=True)
print(x)

y = x + 2
print(y)

z = y*y*2
print(z)

meanSample = z.mean()
print(meanSample)

# Calculating the gradient
meanSample.backward() #dz/dx
print(x.grad)

#backward function can only be created for scalar outputs

tryTwo = y*y*2
print(tryTwo)

#Fixing it
fixing_it = torch.tensor([0.1,1.0,0.001], dtype=torch.float32)
tryTwo.backward(fixing_it)

#Preventing Pytorch from tracking history

# 1. Call the x.requires_grad_(False)
x.requires_grad_(False)
print(x)
# 2. x.detach()
y = x.detach()
print(y)
# 3. Wrap in a with statement with.no_grad()
with torch.no_grad():
    y = x + 2
    print(y)

# Whenever the backward function is called, the gradient for the tensor will be accumulated into .grad attribute
weights = torch.ones(4, requires_grad=True)

for epoch in range (2):
    model_output = (weights*3).sum()

    model_output.backward()

    print(weights.grad)

    # Before the next optimization, Empty the gradient
    weights.grad.zero_()


# Using Pytorch Built in optimizer
optimizer = torch.optim.SGD(weights, lr=0.01)
optimizer.step()
optimizer.zero_grad()