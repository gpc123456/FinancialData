import matplotlib.pyplot as plt
__author__ = 'zoulida'

import pandas as pd
import numpy as np


def box_outliers(ser):
    # 对待检测的数据集进行排序
    new_ser = ser.sort_values()
    # 判断数据的总数量是奇数还是偶数
    if new_ser.count() % 2 == 0:
        # 计算Q3，Q1,IQR
        Q3 = new_ser[int(len(new_ser)/2):].median()
        Q1 = new_ser[:int(len(new_ser)/2)].median()
    elif new_ser.count() % 2 != 0:
        Q3 = new_ser[int(len(new_ser)/2-1):].median()
        Q1 = new_ser[:int(len(new_ser)/2-1)].median()
    IQR = round(Q3-Q1, 1)
    rule = (round(Q3+1.5*IQR, 1) < ser) | (round(Q1-1.5*IQR, 1) > ser)
    index = np.arange(ser.shape[0])[rule]
    # 获取异常值及其索引
    outliers = ser.iloc[index]
    return outliers


excel_data = pd.read_excel('Exp_05_Outlier\data.xlsx')

# 根据data.xlsx文件中value列的数据，画一个箱型图
# 创建数据
# data = np.random.normal((3, 5, 4), (1.25, 1.00, 1.25), (100, 3))
fig = plt.figure()
view = plt.boxplot(excel_data['value'])
plt.show()


outliers = box_outliers(excel_data['value'])
print(outliers)
