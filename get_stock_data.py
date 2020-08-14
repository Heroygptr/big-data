def get_stock_data(stock_number):
    df = ak.stock_zh_a_daily(symbol= stock_number , adjust="hfq")
    df3 = df.reset_index().iloc[-30:,:6]  #取过去30天数据
    df3 = df3.dropna(how='any').reset_index(drop=True) #去除空值且从零开始编号索引
    df3 = df3.sort_values(by='date', ascending=True)
    print df3.head()
    return df3
'''
获取股票最近三十天的数据并显示前五行
''' 