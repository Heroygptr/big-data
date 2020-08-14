#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import dsw

df = dsw.query_stock("shdq").dropna().reset_index()
plot_time = 50

dsw.plot_lines(df, plot_time)

#%%
import dsw

data_sh = dsw.query_stock("shdq")
data_hw = dsw.query_stock("hwdq")
data_xj = dsw.query_stock("xjdq")
data_sj = dsw.query_stock("sjdq")

dsw.plot_comp(data_sh, data_hw, data_xj, data_sj)

# %%
