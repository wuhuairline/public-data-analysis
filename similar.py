from aip import AipNlp
import numpy as np

""" 你的 APPID AK SK """
APP_ID = '5221e74da225460dbcde8bfbac69a2a0'
API_KEY = 'c9b92a17800d4a6e964288fb722ff7d4'
SECRET_KEY = '93178faabac349d1bdc006760251f751'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
data = []
for line in open('D:\桌面文件\研究生\研一课程\大数据分析\课程论文\keywords.txt',encoding='utf-8'):
     data.append(line[:-1])
sim=np.mat(np.zeros((200,200)),dtype=None)
# for i in range(200):
#     for j in range(200):
#         s=client.wordSimEmbedding(data[i], data[j])
#         sim[i,j]=s.get('score')
# np.savetxt('D:\桌面文件\研究生\研一课程\大数据分析\课程论文\similar.csv', sim, delimiter=',')



client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
s=client.wordSimEmbedding('组织','微信')
a=s.get('score')
print(s,a)
print(type(s))