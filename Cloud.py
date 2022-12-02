import os
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS

os.chdir(r'C:\Users\moonchild\OneDrive\MathandModel\NLP\WeiboCrapperAndEmotionAnalysis')
with open(r'res.txt', 'r', encoding="utf-8") as file:
    text = file.read()
print(text)
wordList = " ".join(jieba.lcut(text))
# backgroundImg = np.array(Image.open(r'1129079429_16667011306611n.jpg'))

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
plt.show()
cloud.to_file("Cloud.jpg")

