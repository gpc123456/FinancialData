import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 生成随机点
rng = np.random.default_rng()
x = rng.random(50)
y = 0.8*x + rng.random(50)

# 拟合直线_Scipy
res = stats.linregress(x, y)  # 线性回归
plt.plot(x, y, 'mo', label='原始数据')  # 原始数据散点图
plt.plot(x, res.intercept + res.slope*x, 'g', label='拟合直线')
plt.legend()
plt.title('线性回归_Scipy', fontsize=25)
plt.show()

# 拟合直线_Numpy
res = np.polyfit(x, y, 1)
plt.plot(x, y, 'mo', label='原始数据')  # 原始数据散点图
plt.plot(x, res[0]*x+res[1], 'g', label='拟合直线')
plt.legend()
plt.title('线性回归_Numpy', fontsize=25)
plt.show()
