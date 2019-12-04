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
print(df.mean())

# データを中心化
df_centering = df - df.mean()
print(df_centering.mean())

x_c = df_centering['x']
y_c = df_centering['y']
plt.scatter(x_c, y_c)
plt.show()