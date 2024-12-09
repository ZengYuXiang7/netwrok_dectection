from jenkspy import JenksNaturalBreaks
import numpy as np
import csv
from itertools import combinations
csv_dir = './datasets/MedBIoT/csv/10s/bashlite_leg_10s.csv'

data = []
timestamps = []

with open(csv_dir, 'r') as csv_file :
    reader = csv.reader(csv_file)
    for line in reader:
        data.append(int(line[-1]))
        timestamps.append(line[0])

m = 4   #类别数
GVF = []
same = []
A = list(set(data))
A.sort()
print(len(A))
if m <= 1 or m >= len(A): print(f'类别数m应大于等于1小于等于{len(A)}')
else:
    #列表劈分函数split
    def split(A,B):
        list_tmp = []
        B.insert(0,0)
        B.append(len(A))
        for i in range(len(B)-1):
            list_tmp.append(A[B[i]:B[i+1]])
        return list_tmp
    #列表偏差平方函数SDAM
    def SDAM(A): return sum((i - np.mean(A)) ** 2 for i in A)
    #枚举所有插孔方式
    kong = list(combinations(range(1, len(A)), m-1))
    for i in kong:
        GVF.append(1-(sum(SDAM(j) for j in split(A, list(i))) / SDAM(A)))
    for i in range(len(GVF)):
        if GVF[i] == max(GVF) : same.append(i)
        else: continue
    print(A)
    for k in range(len(same)):
        interval = split(A, list(kong[same[k]]))
        print(f'第{str(k+1)}种分类方式的分类区间为')
        for i in range(len(interval)):
            print(f'第{str(i+1)}类：', end='\t')
            if len(interval) == 1:
                print(f'单点{str(interval[i][0])}自成一类')
            else:
                if i == 0:
                    print(f'[{str(interval[i][0])}, {str(interval[i][-1])}]')
                else:
                    print(f'[{str(interval[i-1][-1])}, {str(interval[i][-1])}]')
                    
    