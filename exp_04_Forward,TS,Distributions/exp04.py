from numpy import *
__author__ = 'zoulida'
# 远期合约的价值
# S代表标的资产价格
# K代表交割价格
# rf代表无风险利率
# time代表权利期间
from math import exp


def forward_value(S, K, rf, time):
    # 远期合约的价值
    f = S-K*exp(-rf*time)
    return f


def forward_price(S, K, rf, time):
    # 远期合约的价格
    F = S*exp(-rf*time)
    return F


S = 930
K = 950
rf = 0.06
time = 0.5
res1 = forward_value(S, K, rf, time)
print('forward_value=', res1)
rest2 = forward_price(S, K, rf, time)
print('forward_price=', rest2)
