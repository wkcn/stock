import tushare as ts
import matplotlib.pyplot as plt

data = [(600547, 601985), (600000, 600887), (600111, 600519)]
#data = [(000630, 600074)]

for ta, tb in data:
    data_a = ts.get_hist_data(str(ta))
    data_b = ts.get_hist_data(str(tb))
    c_a = data_a["close"]
    c_b = data_b["close"]
    plt.subplot(1, 2, 1)
    c_a[0:7].plot()
    plt.subplot(1, 2, 2)
    c_b[0:7].plot()
    plt.show()
    var_a = c_a.var()
    var_b = c_b.var()
    cov = c_a.cov(c_b)
    w_a = (var_b - cov) / (var_a + var_b - 2 * cov)
    w_b = 1.0 - w_a
    print "%d:%lf, %d:%lf" % (ta,w_a,tb,w_b)
