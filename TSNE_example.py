# notie : CTRL + F5 (debugging mode is not working)

from sklearn.manifold import TSNE

from sklearn.datasets import load_iris
from numpy import reshape
import seaborn as sns
import pandas as pd  
import matplotlib.pyplot as plt


iris = load_iris()
x = iris.data
y = iris.target 


tsne = TSNE(n_components=2, verbose=1, random_state=123)
z = tsne.fit_transform(x) 

df = pd.DataFrame()
df["y"] = y
df["comp-1"] = z[:,0]
df["comp-2"] = z[:,1]

sns.scatterplot(x="comp-1", y="comp-2", hue=df.y.tolist(),
                palette=sns.color_palette("hls", 3),
                data=df).set(title="Iris data T-SNE projection") 
plt.show()
'''
x1 =[1, 2, 3]
y1 =[2, 3, 4]
plt.scatter(x1, y1)

'''
print('done')

