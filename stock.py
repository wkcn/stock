#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
fin = open("stock.txt")
stock = {}
for line in fin.readlines():
    line = line.strip()
    if len(line):
        name, tmp = line.split(' (')
        tid = tmp.split(')')[0]
        stock[tid] = name
print len(stock)
