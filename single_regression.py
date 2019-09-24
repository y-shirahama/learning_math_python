import numpy as np

#ベクトル定義
x = np.array([1, 2, 3])
y = np.array([2, 3.9, 6.1])

#データの中心化
xc = x - x.mean()
yc = y - y.mean()

#傾きaの計算
xx = xc * xc
xy = xc * yc

a = xy.sum() / xx.sum()
print(a)