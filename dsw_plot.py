#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import dsw

plot_time = 50     #在此定义画多少天的k线

df = dsw.query_stock("shdq").dropna().reset_index()
dsw.plot_lines(df, plot_time)

#%%
df2 = dsw.query_stock("hwdq").dropna().reset_index()
dsw.plot_lines(df2, plot_time)

#%%
df3 = dsw.query_stock("xjdq").dropna().reset_index()
dsw.plot_lines(df3, plot_time)

#%%
df4 = dsw.query_stock("sjdq").dropna().reset_index()
dsw.plot_lines(df4, plot_time)

#%%
import dsw

data_sh = dsw.query_stock("shdq")
data_hw = dsw.query_stock("hwdq")
data_xj = dsw.query_stock("xjdq")
data_sj = dsw.query_stock("sjdq")

dsw.plot_comp(data_sh, data_hw, data_xj, data_sj)

# %%
