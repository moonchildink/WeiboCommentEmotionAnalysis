import requests
import json

headers = {
    'User=Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
    'Cookie':'PC_TOKEN=de15cf9de8; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW.ah1ZCkrZli1KX4braBpx5JpX5KzhUgL.Fo-4eK54eh.ReKe2dJLoI7f_dcvVqcyDdsBEehz7; WBPSESS=Q4mocWB9j3toNvru27wa1TepLPXtAnu2XAXlhijHDmRDo3c7fhos1X1YsQ5sCQmRNcVN9W4HihTP2x1ITr_j-_bW93ayUrSLA82jgoc18sP1EvFZtdCP_1y9FluueQF5vY73jyYNeLx9uHFkOiAdvQ==; SINAGLOBAL=2129311165616.0813.1669013358502; ULV=1669013911487:2:2:2:5684428808012.402.1669013911365:1669013358503; ALF=1700549732; SUB=_2A25Of1C2DeRhGeNH6lIY8CfEyj-IHXVtDcV-rDV8PUNbmtAfLRTWkW9NSsnp9C-go4Q2I-P2WKyciynFznYmW2Ve; SSOLoginState=1669013734; XSRF-TOKEN=11QMGfwtyRXSFeqt4EtiCVXV; _s_tentry=weibo.com; Apache=5684428808012.402.1669013911365'
}


bilibili_url = r"https://api.bilibili.com/x/v2/reply/main?csrf=3086cea8aed34ae2abe38fd23845c678&mode=3&next=0&oid=254853690&plat=1&seek_rpid=&type=1"

res = requests.get(bilibili_url,headers = headers)

dic = json.loads(res.content)

comment_list = []
while not dic['data']['cursor']['is_end']:

    for reply in dic['data']['replies']:
        comment_list.append(reply['content']['message'])
        if reply['replies'] is not None:
            for replyss in reply['replies']:
                comment_list.append(replyss['content']['message'])
    next = 0
    if not dic['data']['cursor']['is_end']:
        next = dic['data']['cursor']['next']
    next_url = r'https://api.bilibili.com/x/v2/reply/main?csrf=3086cea8aed34ae2abe38fd23845c678&mode=3&next={0}&oid=860715486&plat=1&seek_rpid=&type=1'.format(next)
    dic = json.loads(requests.get(next_url,headers=headers).content)


with open('output\\20230423\\bilibili.txt','a+',encoding='utf-8') as f:
    for i in comment_list:
        f.write(i+'\n')


#%%
## 从文本文件到处excel
import pandas as pd


# comment_list = []
with open("bilibili2.txt",'r',encoding='utf-8') as file:
    li = file.readlines()
li = [i.strip() for i in li]


series = pd.Series(li)
series.head()

series.to_excel('comment0409.xlsx')