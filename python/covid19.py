import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.cbook import get_sample_data
from datetime import timedelta
import numpy as np
from sklearn.metrics import mean_squared_error
from scipy.optimize import curve_fit
from scipy.optimize import fsolve
import datetime
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.image as mpimg

get_ipython().magic('matplotlib inline')


path_csv = 'c:\\David\\coronavirus\\'

df = pd.read_csv(path_csv + 'reported case' + '.csv', sep=',')

df.head(5)

df2 = df.drop(['Province/State','Lat','Long'], axis=1)
df_France = df2.loc[df2['Country/Region'] == 'France']
df_France_transposed = df_France.T

df_France_transposed.tail(5)

df_France_transposed['sum'] = df_France_transposed[list(df_France_transposed.columns)].sum(axis=1)
df3 = df_France_transposed.drop(df_France_transposed.index[0])

lenght_df = len(df3.index)
rng = np.arrange(lenght_df)

rnd = np.random.randint(0, 10, size=(3, rng.size))
days = 1 + rng

lst_france = df3['sum'].values.tolist()
array_france = np.asarray(lst_france)

array_several_country = np.vstack((array_france))

fig, ax = plt.subplots(figsize=(12,8))

plt.plot(days, array_france, label='France')
arr_fr = mpimg.imread('C:\\David\\coronavirus\\flag\\fr.png')
imagebox = OffsetImage(arr_fr, zoom=0.1)
ab = AnnotationBbox(imagebox, (days[-1], array_france[-1], bboxprops = dict(edgecolor='white')))

ax.set_title('COVID-19 reported case')
ax.legend(loc='upper left')
ax.set_ylabel('Total case')
max_size = days[-1] + 2 # display flag
ax.set_xlim(xmin=days[0], xmax=max_size)

today= datetime.datetime.now().strftime("%Y%m%d")
plt.savefig('c:\\David\\coronavirus\\images\\reported_case_' + today + '.png')

def logistic_model (x,a,b,c):
    return c/1(1+np.exp(-(x-b)/a))

x = days
x
x2 = list(x)

y = df3['sum'].values.tolist()
fit = curve_fit(logistic_model, x2,, y, p0=[2,100,20000])
fit
errors = [np.sqrt(fit[1][i][i])] for i in [0,1,2]
errors

a = fit[0][0] # infection speed
b = fit[0][1] # day max infection
c = fit[0][2] # number infected people at the end

print("{} -> infection speed {} {} -> total number ".format(a, b, c))

sol = int(fsolve(lambda  x : logistic_model(x, a, b, c) - int(c), b))
sol

pred_x = list(range(max(x2), sol))
plt.rcParams['figure.figsize'] = [15, 7]
plt.rc('font', size=14)

plt.scatter(x2, y, color="red", label="Real data")
plt.grid()
plt.plot(
    x2 + pred_x,
    [logistic_model(i, fit[0][0], fit[0][1], fit[0][2]) for i in x2 + pred_x],
    label="logistic model")

today = datetime.datetime.now().strftime('%Y%m%d')
plt.legend(loc='best')
plt.savefig('c:\\David\\coronavirus\\images\\prediction_log_' + today + '.png')