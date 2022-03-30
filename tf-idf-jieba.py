import jieba.analyse

file_name = 'D:\桌面文件\研究生\研一课程\大数据分析\课程论文\weibo_clean.txt'
topK =200
content = open(file_name, 'rb').read()

jieba.analyse.set_stop_words('D:\桌面文件\研究生\研一课程\大数据分析\课程论文\stopwords.txt')

print('tf-idf : ')
for x, w in jieba.analyse.extract_tags(content, withWeight=True, topK=topK):
    print(x)
for x, w in jieba.analyse.extract_tags(content, withWeight=True, topK=topK):
    print(w)
    # print('%s %s' % (x, w))

# print('TextRank : ')
# for x, w in jieba.analyse.textrank(content, withWeight=True, topK=topK):
#     print('%s %s' % (x, w))
