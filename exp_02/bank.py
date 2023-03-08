# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv as cs

# 读入ch04_case_transRecord.xlsx文件，将其放置在名为transrecord的dataframe中
transrecord = pd.read_excel('exp_02\\ch04_case_transRecord.xlsx', 'Sheet1')

# 读入ch03_case_binNum.txt文件，因为该txt文件内部是用逗号分隔的卡号-卡种数据对，
# 因此将其当成符号分隔值文件csv读取，并将其转换成dataframe数据对象bcfile

bcfile = cs.reader(open('exp_02\\ch04_case_binNum.txt', 'r', encoding='UTF-8'))

carddata = []
code = []
card = []
for item in bcfile:
    carddata.append(item)

# 因为ch04_case_binNum.txt没有换行，因此carddata是一个嵌套列表，[[data]]
# 其中data本身是一个5556项的列表，然后data是外层列表的唯一列表项
# 所以对这5556项的分别访问要使用双重下标。
size = len(carddata[0])
# 奇数列表项是卡号的前n位，偶数列表项是发卡行信息
count = 0
while (count < size):
    if (count % 2 == 0):
        code.append(carddata[0][count])
    if (count % 2 == 1):
        card.append(carddata[0][count])
    count = count + 1

# 将carddata和code两个列表组合成一个dataframe用于后续数据处理
code2card = pd.DataFrame({'code': code, 'cardinfo': card})


# 将transrecord中的卡号数据列提取出前6个字符,用于生成新的first6列数据
# 使用lambda函数式编程实现
def extractFirst6(s):
    return s[:6]


transrecord['卡号前6位'] = transrecord['卡号'].apply(lambda s: extractFirst6(s))


# 将前6位卡号与carddata中数据进行匹配查找，确定该笔交易的银行卡信息完成
def cardinfo(s):
    t = "".join(list(code2card[code2card.code == s].cardinfo))
    return t


transrecord['卡信息'] = transrecord['卡号前6位'].apply(lambda s: cardinfo(s))

# 将其转换成字符串添加到dataframe的“匹配发卡行”列
pattern1 = '行'
pattern2 = '社'


def matchBank(s):
    t = "".join(list(code2card[code2card.code == s].cardinfo))
    loc = t.find(pattern1)
    if (loc <= 2):
        loc = t.find(pattern2)
    t1 = t[0:loc + 1]
    return t1


transrecord['匹配发卡行'] = transrecord['卡号前6位'].apply(lambda s: matchBank(s))

# 将数据中没有匹配到的空单元格用np.nan填充，然后将其所在行删去
# 将数据中没有匹配到的空单元格\所在行删去
transrecord.loc[transrecord['匹配发卡行'] == ''] = np.nan
transrecord.dropna(inplace=True)

# 按照匹配的发卡行结果对消费金额求和，本例中只有“金额”列是浮点数据，可以进行求和运算
# 找出刷卡金额排在前10的发卡银行
sumbank = transrecord.groupby('匹配发卡行').agg({'金额': 'sum'})
top15bank = sumbank.sort_values(by=['金额'], ascending=False)[:15].copy()

print("刷卡金额排在前15的发卡银行为：")
print(top15bank)

# 绘制图表，这里使用到了matplotlib，后续章节将对其有详细介绍

# get_ipython().run_line_magic('matplotlib', 'inline')
# notebook使用
plt.rcParams['font.sans-serif'] = ['SimHei']

fig, ax = plt.subplots(figsize=(100, 30), dpi=300)
plt.bar(top15bank.index, top15bank['金额'])
ax.set_title('刷卡金额排在前15的发卡银行', fontsize=50, pad=100)
ax.set_ylabel('金额', fontsize=50, labelpad=100)
ax.set_xlabel('发卡银行', fontsize=50, labelpad=100)
plt.xticks(fontsize=50)
plt.yticks(fontsize=50)
plt.savefig("exp_02\\ch04_case_bankcard.png", dpi=300, bbox_inches='tight')
# plt.show()
