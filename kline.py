# 获取股价k线数据
import pandas as pd
import numpy as np
import akshare as ak
import matplotlib
matplotlib.style.use('ggplot') #用于调整图标样式，可选
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick2_ohlc
from matplotlib.ticker import FormatStrFormatter

def k_line(symble, title, last = -30, adjust = "qfq", dprint = False):
  '''
  过去n天个股历史行情均线数据（k线）

  param:
  symble: str,股票编号"sh601727"
  title: str,作图标题
  last: int,过去多少天的数据,默认过去30天，例"-30"
  adjust: str，默认"qfq"前复权,返回复权后数据
  dprint: bool,默认false,是否打印原始数据
  startday: int,行情查询起始日期（懒得转化，没写功能）
  endday: int,行情查询起始日期（懒得转化，没写功能）
  
  '''
  pingan = ak.stock_zh_a_daily(symble, adjust)
  df3 = pingan.reset_index().iloc[last:,:6]  #取过去30天数据
  df3 = df3.dropna(how='any').reset_index(drop=True) #去除空值且从零开始编号索引
  df3 = df3.sort_values(by='date', ascending=True)
  print(df3.info())

  # 均线数据
  df3['5'] = df3.close.rolling(5).mean()
  df3['10'] = df3.close.rolling(10).mean()
  df3.tail()
  
  #画图
  fig, ax = plt.subplots(1, 1, figsize=(8,3), dpi=200)
  candlestick2_ohlc(ax,
                    opens = df3[ 'open'].values,
                    highs = df3['high'].values,
                    lows = df3[ 'low'].values,
                    closes = df3['close'].values,
                    width=0.5, colorup="r",colordown="g")

  # 显示最高点和最低点
  ax.text( df3.high.idxmax(), df3.high.max(),   s =df3.high.max(), fontsize=8)
  ax.text( df3.high.idxmin(), df3.high.min()-2, s = df3.high.min(), fontsize=8)
  ax.set_facecolor("white")
  ax.set_title(title)

  # 画均线
  plt.plot(df3['5'].values, alpha = 0.5, label='MA5')
  plt.plot(df3['10'].values, alpha = 0.5, label='MA10')
  ax.legend(facecolor = 'white', edgecolor = 'white', fontsize = 6)
  # 修改x轴坐标
  plt.xticks(ticks = np.arange(0,len(df3)), labels = df3.date.dt.strftime('%Y-%m-%d').to_numpy() )
  plt.xticks(rotation=90, size=4)
  # 修改y轴坐标
  ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
  plt.show()

k_line(symble = "sh601727", last = -30, adjust = "qfq", dprint = False, title = "上海电气")