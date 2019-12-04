import pandas as pd
import matplotlib.pyplot as plt

# sample.csvの読み込み
# df: data frame
df = pd.read_csv('tmp/sample.csv')
# print(df.head(5))

# 横軸をx,縦軸をyの散布図(scatter)をプロット
x = df['x']
y = df['y']
plt.scatter(x, y)
plt.show()
# print(df.mean())

# データを中心化
df_centering = df - df.mean()
# print(df_centering.mean())

x = df_centering['x']
y = df_centering['y']
plt.scatter(x, y)
plt.show()

# 傾きaの計算
xx = x * x
xy = x * y
a = xy.sum() / xx.sum()
plt.scatter(x, y, label='y')                            # 実測値
plt.plot(x, a*x, label='y_hat', color='red')            # 予測値
plt.legend()
plt.show()