import Analy
import numpy as np

base = '/home/song/Downloads/CPL20210615/TEST'
project = '/2D/MPDO/NewPaper_20210728'
path = base + project + '/field12000'
name = 'field12000.h5'
txt = Analy.CPLtxt(path)
h5 = Analy.CPLh5(name)
txt.read()
field_list = ['Ex', 'Ey', 'Ez',
              'Bx', 'By', 'Bz',
              'Jx', 'Jy', 'Jz']

h5.write('x',np.unique(txt.table['0']))
h5.write('y',np.unique(txt.table['1']))

for i, field in enumerate(field_list):
    data = txt.table[str(i+2)]
    h5.write(field, data)

h5.close()