import jieba
import jieba.posseg
import re
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体
plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题


def get_dict(li):
    dic = {}
    for i in li:
        dic[i] = dic[i].get(i, 0) + 1
    dic = sorted(dic.items(), reverse=True, key=lambda kv: (kv[1], kv[0]))
    return dic


def isMatch(string: str) -> bool:
    if re.match('[\u4e00-\u9fa5]', string):
        return True
    else:
        return False


def is_useful_words(li):
    stopwords = ['我', '了', '在', '和', '是', '作者', '中', '那', '也', '里', '没有', '着', '都', '但', '被', '到',
                 '与', '使',
                 '很', '像', '说', '啊', '把', '又', '他', '之', 'w', 'W', '的', '你们', '你', '我们', '上', '而', '这',
                 '南翔', '可以', 'doge', '就', '系列', '视频', '东西', '人', '吗', '打', 'call', '热词', '真的', '博主',
                 '用', '美食', '做', '不是', '吧', '吃', '至尊', '脱单', '为什么', '至尊', '看', '然后', '大', '辣',
                 '眼睛', '不', '看', '主', '现在', '会', '什么', '主', '就是', '哭', '笑', '能', '知道', '来', '所以',
                 '好像', '因为', '区', '个', '没', '朋友', '不能', '还', '以为', '有', '想', '居然', '已经', '出来',
                 '再', '才', '这个', '这次', '喜欢', '有', '屁', '看到', '给', '这种', '一', 'cry', '帮忙', '下',
                 '下次', '自己', '一定', '这样', '太', '让', '吃瓜', '需要', '觉得', '找', '呢', '每次', '更多', '剩下',
                 '有人', '叫', '直接', '还是', '真', '一直', '呲牙', '后面', '需要', '觉得', '代替'
                                                                                             '一个', '好', '可能',
                 '下期', 'tv', '从', '对', '买', '滑稽', '一个', '怎么', '那个', '薅', '羊毛', '热乎', '谁', '要',
                 '做饭', '回复', '可能', '心心', '奢侈品', '评论', '三连', '不爱', '吃饭', '啦', '这么', '得', '眼',
                 '斜眼', '还有', '大大', '应该', '不会', '跟', '或者', '去', '知识', '的话', '烤全羊', '完', '啥',
                 '手工', '怎么样', '最后', '是不是', '关注', '忘', '写', '开始', '到底', '变成', '呲牙', '大哭', '一只',
                 '量', '站', '多', '她', '子柒', '李子', '这些', '但是', '前', '柒', '过', '呀', '时候', '啊啊啊', '更',
                 '投币', '为', '哇', '逼', '小', '子', '比', '前排']
    li = [i for i in li if i not in stopwords]
    return li


def plot_img(li):
    TOTAL_COUNTS = len(li)
    words = []
    counts = []
    i = 0
    for item in li:
        words.append(item[0])
        counts.append(item[-1] / TOTAL_COUNTS)
        i += 1
        if i > 50:
            break
    plt.figure(figsize=(15, 15))
    plt.barh(words, counts)
    plt.xticks(rotation=90, fontsize=12)
    plt.xlabel("Bilibili热门词汇")
    plt.title("热门词汇，共计$12210$种")
    plt.ylabel("出现频率")
    plt.show()


resList = []
with open(r'output//bilibili2.txt', 'r', encoding='utf-8') as res:
    for i in res:
        resList.append(i)

string = ''
for i in resList:
    string += i
string = string.replace('\n', '')
a = re.sub('\[.*?\]', '', string)
target_word_type = ['n', 'v', 'a']
adj_list = []
verb_list = []
noun_list = []
for i in jieba.posseg.cut(string):
    if i.flag == 'a':
        adj_list.append(i.word)
    elif i.flag == 'v':
        verb_list.append(i.word)
    elif i.flag == 'n':
        noun_list.append(i.word)
