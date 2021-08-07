import h5py as h5
import numpy as np

class CPLtxt:
    def __init__(self, path):
        with open(path, 'r') as f:
            self.lines = f.readlines()
            self.h = len(self.lines)
            self.w = len(self.lines[0].split(' '))
            self.table = {}
            for el in range(self.w):
                self.table[str(el)] = np.zeros(self.l)

    def read(self):
            for i, line in enumerate(self.lines):
                if line == '\n':
                    continue
                else:
                    for name, val in enumerate(line.split(' ')):
                        self.table[str(name)][i] = val

