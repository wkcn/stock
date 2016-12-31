#coding=utf-8
import tushare as ts
fin = open("res.txt")
n = 300
co = [[0.0 for _ in range(n)]for _ in range(n)]
r = 0
szns = ts.get_hs300s()
def T(i):
    return szns["name"][i].decode("utf-8")+szns["code"][i]
for line in fin.readlines():
    sp = line.split()
    for c in range(n):
        co[r][c] = float(sp[c])
    r += 1
for r in range(n):
    for c in range(n):
        if r < c and co[r][c] < -0.8:
            print T(r), T(c), co[r][c]
