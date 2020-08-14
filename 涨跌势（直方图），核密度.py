import pandas as pd
df = pd.read_csv('sh601727.csv')
df.head()
# 剔除缺失数据
df = df.dropna()
df.head()
df = df.reset_index().drop(columns='index')
df.head()
raw_time = pd.to_datetime(df.pop('Unnamed: 0'), format='%Y/%m/%d %H:%M')
from matplotlib import pyplot as plt
import seaborn as sns
# 涨跌幅度
daily_return = df['close'][0::240].pct_change().dropna()
plt.plot(raw_time[0::240][:40], daily_return[:40])
plt.xlabel('Time')
plt.ylabel('Rise and Fall')
plt.show()
# 直方图
plt.hist(daily_return)
# 核密度估计
sns.kdeplot(daily_return)
