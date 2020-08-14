def sort_data(df,number):
    dfn = df.reset_index().iloc[-number:,:6]  #取过去多少天数据
    dfn = dfn.dropna()
    dfn = dfn.reset_index().drop(columns='index')
    dfn = dfn.sort_values(by='date', ascending=True)
    return dfn
''' 数据排序，df是数据，number从以前到今天的数据行数 '''

def get_stock_data(stock_number):
    df = ak.stock_zh_a_daily(symbol= stock_number , adjust="hfq")
    return df
'''获取股票数据，记得加引号''' 

def get_index_data(index_number):
    df = ak.stock_zh_index_daily(symbol= index_number)
    return df
'''获取基金数据，记得加引号 '''