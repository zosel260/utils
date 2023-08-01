import torch
import numpy as np
# import tkinter
# import matplotlib
#matplotlib.use('Qt5Agg')
# matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
#import cv2

print(torch.cuda.is_available())

Z=np.array([[10,0,0],[0,10,0],[0,0,10]])

#Z.show()
# cv2.waitKey(0)

plt.imshow(Z)
plt.show()
