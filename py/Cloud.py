# import jieba
# from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
# import matplotlib.pyplot as plt
# plt.rcParams["font.sans-serif"]=["SimHei"] #设置字体
# plt.rcParams["axes.unicode_minus"]=False #该语句解决图像中的“-”负号的乱码问题
#
# with open(r'D:\code\WeiboCommentEmotionAnalysis\output\20230423\bilibili.txt', 'r', encoding="utf-8") as file:
#     text = file.read()
# print(text)
# wordList = " ".join(jieba.lcut(text))
#
# cloud = WordCloud(
#     width=2000,height=1600
#     , background_color="white"
#     , mode='RGB'
#     # , mask=backgroundImg
#     , max_words=2000
#     , max_font_size=200
#     , font_path=r'C:\Windows\Fonts\simkai.ttf'  # 必须要添加中文字体地址,否则会生成方框
#     , relative_scaling=0.6
#     , random_state=50
#     # , scale=2
#     , stopwords=STOPWORDS.update(
#         ['我', '了', '在', '和', '是', '作者', '中', '那', '也', '里', '没有', '着', '都', '但', '被', '到', '与', '使',
#          '很', '像', '说', '啊', '把', '又', '他', '之', 'w', 'W', '的', '你们', '你', '我们', '上', '而', '这',
#          '一个'])
# ).generate(wordList)
#
# plt.imshow(cloud)
# plt.axis("off")
# plt.title("词云效果图-张洛歌")
# plt.show()
# cloud.to_file("Cloud张洛歌.jpg")
#
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS



wordList = " ".join(jieba.lcut(string))

cloud = WordCloud(
    width=2000,height=1600
    , background_color="white"
    , mode='RGB'
    # , mask=backgroundImg
    , max_words=1000
    , max_font_size=350
    , font_path=r'C:\Windows\Fonts\simhei.ttf'  # 必须要添加中文字体地址,否则会生成方框
    , relative_scaling=0.6
    , random_state=50
    ,colormap='summer'
    , stopwords=STOPWORDS.update(
        ['我', '了', '在', '和', '是', '作者', '中', '那', '也', '里', '没有', '着', '都', '但', '被', '到', '与', '使',
         '很', '像', '说', '啊', '把', '又', '他', '之', 'w', 'W', '的', '你们', '你', '我们', '上', '而', '这','南翔','可以','doge','就','系列','视频','东西','人','吗','打','call','热词','真的','博主','用','美食','做','不是' ,'吧','吃','至尊','脱单','为什么','至尊','看','然后','大','辣','眼睛','不','看','主','现在','会','什么','主','就是','哭','笑','能','知道','来','所以','好像','因为','区','个','没','朋友','不能','还','以为','有','想','居然','已经','出来','再','才','这个','这次','喜欢','有','屁','看到','给','这种','一','cry','帮忙','下','下次','自己','一定','这样','太','让','吃瓜','需要','觉得','找','呢','每次','更多','剩下','有人','叫','直接','还是','真','一直','呲牙','后面','需要','觉得','代替'
         '一个','好','可能','下期','tv','从','对','买','滑稽','一个','怎么','那个','薅','羊毛','热乎','谁','要','做饭','回复','可能','心心','奢侈品','评论','三连','不爱','吃饭','啦','这么','得','眼','斜眼','还有','大大','应该','不会','跟','或者','去','知识','的话','烤全羊','完','啥','手工','怎么样','最后','是不是','关注','忘','写','开始','到底','变成','呲牙','大哭','一只'])
).generate(wordList)

plt.imshow(cloud)
plt.axis("off")
plt.show()
plt.title("词云-张洛歌")
cloud.to_file("output\\20230423\\bilibili_cloud.jpg")