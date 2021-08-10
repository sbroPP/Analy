import Analy
import matplotlib.pyplot as plt
import numpy as np

base = 'field12000'
name = base + '.h5'
save = base + '.png'
h5 = Analy.CPLh5(name)
x = h5.f['x']
y = h5.f['y']
Nx = len(x)
Ny = len(y)
field = np.array(h5.f['Ex']).reshape(Nx, Ny).transpose()
plt.imshow(field)
plt.savefig(save)