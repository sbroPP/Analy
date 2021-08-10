import h5py as h5
import numpy as np

class CPLtxt:
    def __init__(self, path):
        with open(path, 'r') as f:
            self.lines = [line.rstrip() for line in f if len(line) > 1]
            self.h = len(self.lines)
            self.w = len(self.lines[0].split(' '))
            self.table = {}
            for el in range(self.w):
                self.table[str(el)] = np.zeros(self.h)

    def read(self):
            for i, line in enumerate(self.lines):
                for name, val in enumerate(line.split(' ')):
                    self.table[str(name)][i] = float(val)

class CPLh5:
    def __init__(self, path):
        self.f = h5.File(path, 'a')

    def write(self, key, arr):
        dset = self.f.create_dataset(key, data=arr)

    def close(self):
        self.f.close()
