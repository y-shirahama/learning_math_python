import numpy as np
# 重回帰分析のみ読み込み
from sklearn.linear_model import LinearRegression

'''
行列演算の基礎
-ベクトル定義
-行列の定義
-転置
-逆行列
-行列積
'''

# ベクトル定義
x = np.array([[1], [2], [3]])
# print(x)
# print(type(x))

# 行列の定義
X = np.array([
    [1, 2], 
    [3, 4]
])
# print(X)
# print(type(X))

# 転置
Xt = X.T
# print(Xt)

# 逆行列
# linear algebra:線形代数
X_inv = np.linalg.inv(X)
# print(X_inv)

# 行列積
XX_inv = np.dot(X, X_inv)
# print(XX_inv)

'''
下記の列ベクトルx、列ベクトルyの時、重みwを求めよ。
x = [
    [1, 2, 3],
    [1, 2, 5],
    [1, 3, 4],
    [1, 5, 9]
]
y = [
    [1], 
    [5], 
    [6], 
    [8]
]
'''

# Xの定義
X = np.array([
    [1, 2, 3],
    [1, 2, 5],
    [1, 3, 4],
    [1, 5, 9]
])

# yの定義
y = np.array([
    [1],
    [5],
    [6],
    [8]
])

# Step1:X転置行列を取得
XtX = np.dot(X.T, X)
# print(XtX)

# Step2:X転置行列の逆行列を取得
Xtx_inv = np.linalg.inv(XtX)
# print(Xtx_inv)

# Step3:y転置行列を取得
Xty = np.dot(X.T, y)
# print(Xty)

# Step4:重みwを求める
w = np.dot(Xtx_inv, Xty)
# print(w)

'''
[[-0.14285714]
 [ 0.71428571]
 [ 0.57142857]]
'''

# モデルの宣言
model = LinearRegression()

'''
モデルの学習

線形回帰モデルのパラメータ調整を実行。
xが対象データ、yが正解データ(教師あり学習が前提)
'''
model.fit(X, y)

# 回帰変数と回帰直線の切片
print(model.coef_)
print(model.intercept_)

'''
予測精度

予測値xと正解値yの相関を図り、決定係数を出力する。
'''
print(model.score(X, y))

'''
予測値の計算

モデルを私用して、xに対して予測を実行し予測値を算出する。
'''
print(model.predict(X))