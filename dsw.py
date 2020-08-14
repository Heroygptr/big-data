import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns
import plotly as ly
import akshare as ak
import numpy as np
import datetime

import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick2_ohlc
from matplotlib.ticker import FormatStrFormatter
from matplotlib import ticker as mticker  # 刻度处理
from matplotlib import dates as mdates  # 时间格式处理
from matplotlib.pyplot import MultipleLocator

query_dis = {"shdq":"sh601727", "hwdq":"sh603063", \
    "xjdq":"sz000400", "sjdq":"sz300444"}

def query_stock(stock_name):
    stock = ak.stock_zh_a_daily(symbol = query_dis[stock_name], adjust="hfq")
    return stock

def query_shdq():
    #上海电气
    stock = query_stock("shdq")
    return stock

def query_hwdq():
    #禾望电气
    stock = query_stock("hwdq")
    return stock

def query_xjdq():
    #许继电气
    stock = query_stock("xjdq")
    return stock

def query_sjdq():
    #双杰电气
    stock = query_stock("sjdq")
    return stock

def datef_p_strf(data, date_format):     #date-dateformat时  导出str-rawtime
    dates = data['date']  
    raw_time = []

    for i in dates:
        raw_time.append(i.strftime(date_format))
    return raw_time

def strf_p_datef(data, date_format):    #date-str时  导出dateform-date
    raw_time = data.pop('date')  
    dates = []

    for i in raw_time:
        dates.append(datetime.datetime.strptime(i, date_format))
    
    data['date'] = dates
    return dates

def data_300(data):
    data_ = data.iloc[-300:, :]
    return data_

def plot_comp(df1, df2, df3, df4):
    df1 = data_300(df1)
    df2 = data_300(df2)
    df3 = data_300(df3)
    df4 = data_300(df4)

    fig, ax = plt.subplots()
    df1.plot(ax=ax, y='close', label='01')
    df2.plot(ax=ax, y='close', label='02')
    df3.plot(ax=ax, y='close', label='03')
    df4.plot(ax=ax, y='close', label='04')

    plt.legend(loc='upper left')

def w_spin(ax):
    ax.spines['bottom'].set_color('w') 
    ax.spines['top'].set_color('w') 
    ax.spines['left'].set_color('w') 
    ax.spines['right'].set_color('w')

def w_tick(ax):
    ax.tick_params(axis='y', colors='w')  
    ax.tick_params(axis='x', colors='w')

def plot_lines(data, plot_time):
    data_plot = data.iloc[-plot_time:]
    fig = plt.figure(facecolor='#07000d', figsize=(15, 10))  # 画布
    ax = plt.subplot2grid((6, 4), (1, 0), rowspan=4,colspan=4, facecolor='#07000d')  

    ax.grid(True, color='w', axis = 'y')  # 网格
    ax.grid(True, axis = 'x', alpha = 0.3) 

    ax.yaxis.label.set_color('w')  # 轴
    plt.ylabel('Stock Price and Volume', color='w')  
    w_spin(ax)
    w_tick(ax)

    #================================================

    candlestick2_ohlc(ax,
                    opens = data_plot[ 'open'].values,
                    highs = data_plot['high'].values,
                    lows = data_plot[ 'low'].values,
                    closes = data_plot['close'].values,
                    width=0.5, colorup='red', colordown='lime')

    #修改xy坐标
    plt.xticks(ticks =  np.arange(0,len(data_plot)), labels = data_plot.date.dt.strftime('%Y-%m-%d').to_numpy(), rotation=80, size=8)
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  # 横轴-时间

    #=====================================
    plot_mat = pd.DataFrame()
    plot_mat['close'] = data['close']

    mov_avg_ten = plot_mat['close'].rolling(window=5).mean() # 每x天收盘价的均值，向下滚动1天
    mov_avg_thirty = plot_mat['close'].rolling(window=10).mean()  
    ax.plot(range(plot_time), mov_avg_ten.iloc[-plot_time:], 'lightyellow', label='short_time', linewidth=1.5)  
    ax.plot(range(plot_time), mov_avg_thirty.iloc[-plot_time:], 'cyan', label='long_time', linewidth=1.5)

    #====================================
    # 成交量图
    Volume = data_plot[['date', 'volume']].groupby(by='date').sum().reset_index()

    ax_1 = ax.twinx()  # 共享绘图区域
    ax_1.fill_between(range(plot_time), 0, Volume.volume.values,facecolor='#00ffe8', alpha=0.4)  
    ax_1.grid(False) 
    ax_1.set_ylim(0, 4*Volume.volume.values.max())  

    w_spin(ax_1)
    w_tick(ax_1)

    #======================================
    #涨跌幅图
    ax_2 = plt.subplot2grid((6, 4), (0, 0), sharex=ax, rowspan=1, colspan=4, facecolor='#07000d') 
    data_plot2 = data.iloc[-plot_time-1:]
    raw_time = datef_p_strf(data_plot, '%Y-%m-%d')

    daily_return = data_plot2['close'].pct_change().dropna()
    ax_2.plot(raw_time, daily_return, 'cyan', linewidth = 2)
    plt.ylabel('Rise and Fall', color = 'w')
    ax_2.axhline(0.03, color='lightcoral')  
    ax_2.axhline(0, color='lightgreen')  
    ax_2.set_yticks([0, 0.03])

    ax_2.fill_between(raw_time, daily_return, 0.03, where=(daily_return >= 0.03),\
        facecolors='lightcoral') 
    ax_2.fill_between(raw_time, daily_return, 0, where=(daily_return <= 0),\
        facecolors='lightgreen')

    w_spin(ax_2)
    ax.tick_params(axis='y', colors='w')
    # plt.savefig('dsw_test.jpg')
    #========================================
    plt.show()
