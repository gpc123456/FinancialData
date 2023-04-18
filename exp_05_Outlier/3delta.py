__author__ = 'zoulida'
import numpy as np
import pandas as pd


def three_sigma(ser):
    '''
    ser参数：被检测的数据，接收DataFrame的一列数据
    返回：异常值及其对应的行索引
    '''
    # 计算平均值
    mean_data = ser.mean()
    # 计算标准差
    std_data = ser.std()
    # 小于μ-3σ或大于μ+3σ的数据均为异常值
    rule = (mean_data-3*std_data > ser) | (mean_data+3*std_data < ser)
    # 然后np.arange方法生成一个从0开始，到ser长度-1结束的连续索引，再根据rule列表中的True值，直接保留所有为True的索引，也就是异常值的行索引
    index = np.arange(ser.shape[0])[rule]
    # 获取异常值
    outliers = ser.iloc[index]
    return outliers


# 读取data.xlsx文件
excel_data = pd.read_excel('Exp_05_Outlier\data.xlsx')
# 对value列进行异常值检测，只要传入一个数据列
outliers = three_sigma(excel_data['value'])
print(outliers)
