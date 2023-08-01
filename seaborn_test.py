import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x = np.arange(1, 10, 0.5)
y = np.random.randint(1, 10, size=len(x))

sns.set_style('whitegrid')
sns.scatterplot(x=x, y=y)
plt.show()
print('done')
