import numpy as np

'''
行列演算の基礎
-ベクトル定義
-行列の定義
-転置
-逆行列
-行列積
'''

# ベクトル定義
x = np.array([1, 2, 3])
print(x)
print(type(x))

# 行列の定義
X = np.array([[1, 2], [3, 4]])
print(X)
print(type(X))

# 転置
Xt = X.T
print(Xt)

# 逆行列
# linear algebra:線形代数
X_inv = np.linalg.inv(X)
print(X_inv)

# 行列積
XX_inv = np.dot(X, X_inv)
print(XX_inv)