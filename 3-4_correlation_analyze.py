#-*- coding: utf-8 -*-
#餐饮销量数据相关性分析
import pandas as pd
import seaborn as sns

catering_sale = r'D:\桌面文件\研究生\研一课程\大数据分析\class3\class3\catering_sale_all.xls' #餐饮数据，含有其他属性
data = pd.read_excel(catering_sale, index_col = u'日期') #读取数据，指定“日期”列为索引列

data.corr() #相关系数矩阵，即给出了任意两款菜式之间的相关系数
data.corr()[u'百合酱蒸凤爪'] #只显示“百合酱蒸凤爪”与其他菜式的相关系数
data[u'百合酱蒸凤爪'].corr(data[u'翡翠蒸香茜饺']) #计算“百合酱蒸凤爪”与“翡翠蒸香茜饺”的相关系数


sns.set(style="ticks")
#
df = sns.load_dataset("iris")
# sns.pairplot(df, hue="species")