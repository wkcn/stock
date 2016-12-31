#coding=utf-8
import tushare as ts
import matplotlib.pyplot as plt
import numpy as np

sz50s = ts.get_sz50s()
k = 1
grid_r = 3
grid_c = 3
for tid in sz50s["code"].values: 
    data = ts.get_hist_data(tid, start = '2000-01-01', end = '2016-12-31')
    close_data = data["close"]
    plt.subplot(grid_r, grid_c, k)
    std = close_data.std()
    mean = close_data.mean()
    plt.title("[%s]mean: %.3lf, std: %.3lf" % (tid, mean, std))
    vs = close_data.values
    z = vs[0] - np.mean(vs[1:8])
    color = 'g'
    if z > 0:
        color = 'r'
    close_data.plot(color = color)
    if k == grid_r * grid_c:
        plt.show()
        k = 1
    else:
        k += 1
