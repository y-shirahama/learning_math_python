import pandas as pd

# sample.csvの読み込み
# df: data frame
df = pd.read_csv('./tmp/sample.csv')
# print(df)

# 先頭レコードから指定のレコード数を表示
print(df.head(5))

# データの抽出
x = df['x']
y = df['y']

print(x)
print(y)