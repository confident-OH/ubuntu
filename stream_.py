import numpy as np
array = np.array([[2, 4], [3, 5.9], [4, 8.4], [5, 11], [6, 11.8], [7, 14.5]])
weight = np.array([[2.5, 0]])
def determine (weight, array):
    item = array.T
    x_array = item[0]
    x_array = x_array.reshape(1, 6)
    y_array = item[1]
    y_array = y_array.reshape(1, 6)
    item = x_array * weight[0][0] - y_array
    return np.sum(item)
while determine(weight, array)>0.1 or determine(weight, array)<-0.1:
    item = array.T
    x_array = item[0]
    x_array = x_array.reshape(1, 6)
    y_array = item[1]
    y_array = y_array.reshape(1, 6)
    item = x_array * weight[0][0] - y_array
    item = item.reshape(1, 6)
    item2 = item * x_array
    item2 = item2.reshape(1, 6)
    weight[0][0] -= 0.01 * item2.sum()
    weight[0][1] -= 0.01 * item.sum()
print(weight)