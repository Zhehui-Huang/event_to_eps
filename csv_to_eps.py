from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
import os

path = os.path.join(os.getcwd(), "csv")
print(path)
files= os.listdir(path)
s = []
for ff in files:
    if not os.path.isdir(ff):
        file = os.path.join(path, ff)
        print(file)
        style.use('ggplot')

        x, y = np.loadtxt(file,
                       unpack=True,
                       delimiter=';')
        plt.cla()

        plt.plot(x, y)

        plt.title('lasertag_three_opponents_small')

        plt.ylabel(os.path.splitext(ff)[0])

        plt.xlabel('Environment Frames')

        plt.savefig(os.path.join(os.getcwd(),"eps", os.path.splitext(ff)[0] + ".eps"), format='eps')



