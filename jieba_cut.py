# -*- coding: utf-8 -*-
import jieba

txt = open(r"D:\桌面文件\研究生\徐门\小论文1\数据\weibo_clean.txt", "r", encoding='utf-8').read()
words = jieba.cut(txt)     # 使用精确模式对文本进行分词
stwlist=[line.strip()for line in open('D:\桌面文件\研究生\徐门\小论文1\数据\stopwords.txt',encoding='utf-8').readlines()]

word_ = {}
for word in words:
    if word.strip() not in stwlist:
        if len(word) > 1:
            if word != '\t':
                if word != '\r\n':
                    # 计算词频
                    if word in word_:
                        word_[word] += 1
                    else:
                        word_[word] = 1

# 将词汇和词频以元组的形式保存
word_freq = []
for word, freq in word_.items():
    word_freq.append((word, freq))

#降序排列
word_freq.sort(key=lambda x: x[1], reverse=True)
print(word_freq[0:500])
dic=dict(word_freq[0:500])
# Word=[]
# for i in range(500):
#   Word.append(word_freq[i][0])
from wordcloud import WordCloud,ImageColorGenerator
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
image = Image.open('D:\桌面文件\研究生\徐门\小论文1\图\cld1.jpg')  # 作为背景轮廓图
graph = np.array(image)
# color_mask = imageio.imread("D:\桌面文件\研究生\研一课程\大数据分析\课程论文\cld.png")
wc = WordCloud(background_color="white",font_path='C:\Windows\Fonts\STSONG',max_words=500,min_font_size=10,max_font_size=60,scale=2,mask=graph,width=2000,height=1200)
wc.generate_from_frequencies(dic)
# i = str('why')
# wc.generate(word_freq[0:500])
# plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
image_color = ImageColorGenerator(graph)
# wc.recolor(color_func=image_color)
plt.figure()
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()
# wc.to_file(str(i)+".png")

# from wordcloud import WordCloud
# from pyecharts import options as opts
# from pyecharts.charts import Liquid
# from pyecharts.globals import SymbolType
# word_cloud = WordCloud.add("", word_freq[0:500], word_size_range=[20, 100], shape=SymbolType.DIAMOND).set_global_opts(title_opts=opts.TitleOpts(title="词云图"))
# word_cloud.render('D:\桌面文件\研究生\研一课程\大数据分析\课程论文\word_cloud.html')
    # for word in words:
#     if len(word) == 1:    # 单个词语不计算在内
#         continue
#     else:
#         counts[word] = counts.get(word, 0) + 1    # 遍历所有词语，每出现一次其对应的值加 1
#
# items = list(counts.items())
# items.sort(key=lambda x: x[1], reverse=True)    # 根据词语出现的次数进行从大到小排序
#
# fp=open('save-0919.txt', 'w+')
# for i in items:
#     fp.write(str(i[0])+'\t'+str(i[1])+'\n')
#
# fp.close();