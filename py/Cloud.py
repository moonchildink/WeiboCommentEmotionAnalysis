import jieba
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"]=["SimHei"] #设置字体
plt.rcParams["axes.unicode_minus"]=False #该语句解决图像中的“-”负号的乱码问题

with open(r'D:\code\WeiboCommentEmotionAnalysis\output\20230423\bilibili.txt', 'r', encoding="utf-8") as file:
    text = file.read()
print(text)
wordList = " ".join(jieba.lcut(text))

cloud = WordCloud(
    width=2000,height=1600
    , background_color="white"
    , mode='RGB'
    # , mask=backgroundImg
    , max_words=2000
    , max_font_size=200
    , font_path=r'C:\Windows\Fonts\simkai.ttf'  # 必须要添加中文字体地址,否则会生成方框
    , relative_scaling=0.6
    , random_state=50
    # , scale=2
    , stopwords=STOPWORDS.update(
        ['我', '了', '在', '和', '是', '作者', '中', '那', '也', '里', '没有', '着', '都', '但', '被', '到', '与', '使',
         '很', '像', '说', '啊', '把', '又', '他', '之', 'w', 'W', '的', '你们', '你', '我们', '上', '而', '这',
         '一个'])
).generate(wordList)

plt.imshow(cloud)
plt.axis("off")
plt.title("词云效果图-邢智博")
plt.show()
cloud.to_file("Cloud20230504.jpg")

