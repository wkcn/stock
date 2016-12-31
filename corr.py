#coding=utf-8
import tushare as ts
import matplotlib.pyplot as plt

gp = open("gp.txt", "w")
fout = open("res.txt", "w")
s = ts.get_hs300s()
n = 300
ds = []
print s
for tid in s["code"].values:
    print (tid)
    gp.write(tid)
    gp.write("\n")
    data = ts.get_hist_data(tid)
    ds.append(data)

co = [[0.0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i < j:
            co[i][j] = ds[i]["close"].corr(ds[j]["close"])


for i in range(n):
    for j in range(n):
        if i < j:
            fout.write(str(co[i][j]))
        elif i == j:
            fout.write("1.0")
        else:
            fout.write(str(co[j][i]))
        fout.write(" ")
    fout.write("\n")

fout.close()
