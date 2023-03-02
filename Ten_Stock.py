import akshare as ak
import pandas as pd

stock_id = ["000001", "000002", "000004", "000005", "000006",
            "000007", "000008", "000009", "000010", "000012"]

stock_df = pd.DataFrame(columns=['日期', "股票代码", "股票简称", "涨跌幅"])

for item in stock_id:
    stock = ak.stock_zh_a_hist(
        symbol=item, period="daily", start_date="20230301", end_date='20230301', adjust="hfq")
    stock_individual_info = ak.stock_individual_info_em(symbol=item)
    stock_item = []
    stock_item.append(stock.loc[0, "日期"])
    stock_item.append(item)
    stock_item.append(stock_individual_info.loc[5, "value"])
    stock_item.append(stock.loc[0, "涨跌幅"])
    stock_df.loc[len(stock_df.index)] = stock_item

stock_df_sort = stock_df.sort_values(
    by="涨跌幅", ascending=False, ignore_index=True)

print("保存为csv"+'\n')
stock_df.to_csv("stock.csv")

print("涨幅最大的股票为：")
print(stock_df_sort.loc[0, "股票代码"]+","+stock_df_sort.loc[0, "股票简称"])

print("跌幅最大的股票为：")
print(stock_df_sort.loc[len(stock_df.index)-1, "股票代码"] +
      ","+stock_df_sort.loc[len(stock_df.index)-1, "股票简称"])
