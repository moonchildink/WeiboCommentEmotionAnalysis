import requests
import os
from bs4 import BeautifulSoup
import re


os.chdir(r'C:\Users\moonchild\OneDrive\MathandModel\NLP\WeiboCrapperAndEmotionAnalysis')


headers = {
    'User=Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
    'Cookie':'PC_TOKEN=de15cf9de8; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW.ah1ZCkrZli1KX4braBpx5JpX5KzhUgL.Fo-4eK54eh.ReKe2dJLoI7f_dcvVqcyDdsBEehz7; WBPSESS=Q4mocWB9j3toNvru27wa1TepLPXtAnu2XAXlhijHDmRDo3c7fhos1X1YsQ5sCQmRNcVN9W4HihTP2x1ITr_j-_bW93ayUrSLA82jgoc18sP1EvFZtdCP_1y9FluueQF5vY73jyYNeLx9uHFkOiAdvQ==; SINAGLOBAL=2129311165616.0813.1669013358502; ULV=1669013911487:2:2:2:5684428808012.402.1669013911365:1669013358503; ALF=1700549732; SUB=_2A25Of1C2DeRhGeNH6lIY8CfEyj-IHXVtDcV-rDV8PUNbmtAfLRTWkW9NSsnp9C-go4Q2I-P2WKyciynFznYmW2Ve; SSOLoginState=1669013734; XSRF-TOKEN=11QMGfwtyRXSFeqt4EtiCVXV; _s_tentry=weibo.com; Apache=5684428808012.402.1669013911365'
}


def getComment(ID,UID):
    """
    @params:ID,当前这条微博的ID
    @params:UID,用户ID
    """
    URL = r'https://weibo.com/ajax/statuses/buildComments'
    params = {
        'flow':0,
        'is_reload':1,
        'id':ID,            # 当前微博的ID
        "is_show_bulletin":2,
        'is_mix':0,
        'count':50,
        'uid':UID           # 用户ID
    }
    temp = requests.get(url=URL,headers=headers,params=params)
    temp = temp.json()
    """
    返回所有数据,注意或得到的json数据的格式:
    ok:1,
    filter_gorup:0/1,    分别是按热度排序和按时间排序
    data:[],              数组,是所需要的评论数据,其中每一个又是一个json()格式数据,source可以获取到IP属地,text_raw是原始评论文本
    rootComment,
    total_number,
    max_id:              下一条数据请求头之中的max_id
    trendsText
    """
    resData = [temp['data']]
    nextMaxId = temp['max_id']        # 可以观测到评论的第一次请求没有max_id属性,最后一次评论请求的response之中
    while nextMaxId!=0:
        params['max_id'] = nextMaxId
        temp = requests.get(URL,headers=headers,params=params).json()
        resData.append(temp['data'])
        nextMaxId = temp['max_id']
    # resData的结构:第一层为数组,包含本次获取的所有评论,数组之内是json数据
    return resData


def getTextFromRes(resList):
    newList = []
    for i in range(len(resList)):
        for j in range(len(resList[i])):
            newList.append(resList[i][j]['text_raw'])

    return newList

""""
https://weibo.com/ajax/statuses/buildComments?flow=0&is_reload=1&id=&is_show_bulletin=2&is_mix=0&max_id=138864120679053&count=20&uid=
"""
URL = r'https://weibo.com/ajax/statuses/buildComments'
ID = 4841870633468410
UID = 1764523734
res = getComment(ID,UID)
res = getTextFromRes(res)
with open('res.txt','w',encoding='utf-8') as f:
    for i in res:
        f.write(i+'\n')
