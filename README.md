# analysis of SHANGHAI ELECTRIC(sh601727)
这个项目对上海电气的股票信息进行了整理和分析<br>
大盘情况和上海电气股价涨跌简析请看`上证和上海电气指数图`<sup>hzy</sup>，参考内容移步`参考资料`。  

`Kline`<sup>nzg</sup>绘制了K线图与5、10日均线。 

`涨跌势（直方图），核密度`<sup>wkl</sup>绘制了直方图。  

`dsw_plot`<sup>dsw</sup>绘制了四只股票的比较（包括kline、成交量、涨跌幅、唐奇安通道等）。

# 功能
`上证和上海电气指数图`封装了两个取用的函数，一个排序的函数用以获取处理数据，取得大盘1000条数据，上海电气1000条数据调用plotly绘制成**互动式图表**，并结合资料给出一定分析。使用jupyter notebook打开就能看到运行结果。  

`kline`功能：便捷获取一段时间内某股票的历史行情数据，可调整多种赋权方式，绘出（或打印出）原始数据、不同赋权后数据、5日、10日均线（可调整）。

`涨跌势（直方图），核密度`输出涨跌势（直方图），核密度。  

`dsw.py`中**存放制图函数**，具体内容包括**查询股票**，在**kline**的基础上绘制**成交量线**、**填充**涨跌势线，以及**唐奇安通道**和收盘价的对比。另外还有四只上海**股票的比较**(由于字体输出问题，我用1234的代号分别代表这四只股票)。  
`dsw_plot.py`是调用`dsw.py`中的函数，生成**各个股票的数据图**以及四只股票之间的**对比图**。
`dsw_plot.ipynb`是`dsw_plot.py`的notebook形式输出。

# 团队
* [董思雯](https://github.com/liquor-d) - 针对四支股票进行了一些数据比较，提供技术支持，明确了团队任务分配。
* [王可立](https://github.com/Heroygptr) - 绘制成涨跌势与核密度，创立仓库积极配合队友。
* [牛志刚](https://github.com/NiuZG) - 绘制n天可持续K线均线，帮助队友熟悉github流程工作。
* [何振远](https://github.com/Smiille) - 绘制大盘趋势与上海电气股价图，查找了许多参考资料并制作了readme。

# 致谢
* 感谢老师和助教的指导和帮助
* 感谢队友全心全意的付出和工作
* 感谢其他队伍同学的鞭策和激励  