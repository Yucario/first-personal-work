import jieba
import re
from os import path  #用来获取文档的路径
import os
from PIL import Image
import numpy as  np
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator
import matplotlib.font_manager as fm

jieba.add_word('逆行者')

text_path="video.txt"  
text=open(text_path,encoding="utf8").read()     #读取评论文件

def seg_depart(sentence):
    # 对文档中的每一行进行中文分词
    s=""
    sentence_depart = jieba.lcut(sentence.strip())
    for w in sentence_depart:
        if len(w)>1:
            s+=w
    sentence_depart = jieba.cut(s)
    return sentence_depart

depart = seg_depart(text)

fW = open('bbb.txt', 'w', encoding='UTF-8')
fW.write(' '.join(depart))
fW.close()

d=os.path.dirname(os.path.realpath('__file__'))
bg=np.array(Image.open(path.join(d, "wuhan.jpg")))
text_path="bbb.txt"
#读取要分析的文本，读取格式
text=open(path.join(d,text_path),encoding="utf8").read()

#生成
wc=WordCloud(
    background_color="white",
    max_words=600,            #设置图片的背景
    #max_font_size=100,
    #random_state=32,
    mask=bg,  # 设置背景图片
    max_font_size=150,  # 字体最大值
    random_state=32,
    width=1000, height=900, margin=2,
    font_path='C:/Windows/Fonts/simkai.ttf'   #中文处理，用系统自带的字体
    ).generate(text)

#为图片设置字体
my_font=fm.FontProperties(fname='C:/Windows/Fonts/simkai.ttf')
#产生背景图片，基于彩色图像的颜色生成器
image_colors=ImageColorGenerator(bg)
#开始画图
plt.imshow(wc,interpolation="bilinear")
#为云图去掉坐标轴
plt.axis("off")
#画云图，显示
#plt.figure()
plt.show()
#为背景图去掉坐标轴
plt.axis("off")
#plt.imshow(bg,cmap=plt.cm.gray)
#plt.show()

#保存云图
wc.to_file("aa.png")
