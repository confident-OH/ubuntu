import numpy as np
a = []
for i in range(9):
    name = int(input("Please enter"))
    a.append(name)
arr = np.array([a])
print(arr)
print(arr.shape)