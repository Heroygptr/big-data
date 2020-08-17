from datetime import datetime
import backtrader as bt
import matplotlib.pyplot as plt
import akshare as ak
#先设置中文绘图全局
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

#回测函数
def backtest(name, strategy, sy=2000, sm=1, sd=1, ey=2020, em=8, ed=1, start_cash = 1000000, commission = 0.002, plot=True ):
    '''
    *param*
    dataname: 
    strategy: 我的策略，一个类
    sy, sm, sd (ey, em, ed): 回测开始\回测结束时间2000, 1, 1
    start_cash: 初始资本默认1000000, 
    commission: 交易手续费默认为 0.002  (0.2%)
    '''
 
    '''函数测试变量
    print("回测开始时间:")
    sy=input("年:")
    sm=input("月:")    
    sd=input("日:")
    print("回测结束时间:")
    ey=input("年:")
    em=input("月:")    
    ed=input("日:")
    start_date = datetime(2000, 1, 1)  # 回测开始时间
    end_date = datetime(2020, 1, 1)  # 回测结束时间'''
    #先设置中文绘图全局
    plt.rcParams["font.sans-serif"] = ["SimHei"]
    plt.rcParams["axes.unicode_minus"] = False
    cerebro = bt.Cerebro()  # 初始化回测系统
    start_date = datetime(sy, sm, sd)  # 回测开始时间
    end_date = datetime(ey, em, ed)  # 回测结束时间

    data = bt.feeds.PandasData(dataname=name, fromdate=start_date, todate=end_date)  # 加载数据
    cerebro.adddata(data)  # 将数据传入回测系统
    cerebro.addstrategy(strategy)  # 将交易策略加载到回测系统中
    
    cerebro.broker.setcash(start_cash)  # 设置初始资本为 100000
    cerebro.broker.setcommission(commission)  # 设置交易手续费为 0.2%
    cerebro.run()  # 运行回测系统

    port_value = cerebro.broker.getvalue()  # 获取回测结束后的总资金
    pnl = port_value - start_cash  # 盈亏统计

    print(f"初始资金: {start_cash}\n回测期间：{start_date.strftime('%Y%m%d')}:{end_date.strftime('%Y%m%d')}")
    print(f"总资金: {round(port_value, 2)}")
    print(f"净收益: {round(pnl, 2)}")
    if plot==1:
        cerebro.plot(style='candlestick')  # 画图 