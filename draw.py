import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 10000)

y1 = x ** 2
y2 = x**3 + x**4

plt.figure()
plt.xlim(-2, 2)
plt.ylim(-2, 2)
x_interval = np.linspace(-2, 2, 11)
plt.xticks(x_interval)
plt.yticks([-2, -1, 0, 1, 2], ['level1', 'level2', 'level3', 'level4', 'level5'])
plt.xlabel('price')
plt.ylabel('number')
aa, = plt.plot(x, y1, color = 'red', linewidth = 5, linestyle = '--')
bb, = plt.plot(x, y2, color = 'green', linewidth = 1, linestyle = '-')
plt.legend(handles = [aa, bb], labels = ['test1', 'test2'], loc = 'lower right')
a = plt.gca()
a.spines['right'].set_color('none')
a.spines['top'].set_color('none')
a.xaxis.set_ticks_position('bottom')
a.yaxis.set_ticks_position('left')
a.spines['bottom'].set_position(('data', 0))
a.spines['left'].set_position(('data', 0))
print(plt.show())
