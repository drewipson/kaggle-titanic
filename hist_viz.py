import numpy as np
import pandas as pd
import matplotlib as p
p.use("TkAgg")
import matplotlib.pyplot as plt
df_train = pd.read_csv("./train.csv")

hist_men = df_train.Age[df_train.Sex == 'male']
hist_women = df_train.Age[df_train.Sex == 'female']

mA = plt.hist(hist_men, 10, orientation='horizontal', density=0, rwidth=0.8, label='Male', color='blue')
fA = plt.hist(hist_women, bins=mA[1], orientation='horizontal', density=0,rwidth=0.8,label='Women',color='pink')

for p in fA[2]:
	p.set_width( - p.get_width())
xmin = min([ min(w.get_width() for w in fA[2]),
	min([w.get_width() for w in mA[2]]) ])
xmin = np.floor(xmin)
xmax = max([ max(w.get_width() for w in fA[2]), 
                max([w.get_width() for w in mA[2]]) ])
xmax = np.ceil(xmax)
range = xmax=xmin
delta = 0.0 * range
plt.xlim([xmin - delta, xmax + delta])
xt = plt.xticks()
n = xt[0]
s = ['%.1f'%abs(i) for i in n]
plt.xticks(n, s)
plt.legend(loc='best')
plt.axvline(0.0)
plt.show()
