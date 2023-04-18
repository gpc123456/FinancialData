__author__ = 'zoulida'

import pylab
import random

# days to generate data for
duration = 100
# mean value
mean_inc = 0

# standard deviation
std_dev_inc = 2

# time series
x = range(duration)
y = []
price_today = 0

for i in x:
    # 正态分布，均值0，标准差2
    next_delta = random.normalvariate(mean_inc, std_dev_inc)
    price_today += next_delta
    y.append(price_today)

pylab.plot(x, y)
pylab.xlabel("Time")
pylab.ylabel("Value")
pylab.show()
