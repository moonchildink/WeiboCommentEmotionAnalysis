
import json
import csv
import re
import requests
import time


# 获取网页源码的文本文件
def get_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
        "Referer": "https://m.weibo.cn"
    }
    cookies = {
        "cookie": "PC_TOKEN=f664ebf936; SUB=_2A25JJep4DeRhGeNH6lIY8CfEyj-IHXVq6fYwrDV8PUJbkNAbLRD3kW1NSsnp9COCJASPmS8SL8eznaW_jNpmYpXI; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW.ah1ZCkrZli1KX4braBpx5NHD95Qf1K271K541h20Ws4DqcjSdgvadJSQIgp.eo5Ee5tt; _s_tentry=passport.weibo.com; Apache=1890978307128.346.1679923721048; SINAGLOBAL=1890978307128.346.1679923721048; XSRF-TOKEN=502jjIS2KPtPbs4SJkMeZvTL; WBPSESS=Q4mocWB9j3toNvru27wa1TepLPXtAnu2XAXlhijHDmRDo3c7fhos1X1YsQ5sCQmR4VXzAVYCORzoN9NMivkTmb1wioIqgdKlXfZovDWx2B-sqmzqbYyGOfskdSmGnl940Z8i2ODL_1QG5rTT9EoZSQ==; ULV=1679923727783:1:1:1:1890978307128.346.1679923721048:; login_sid_t=13b601d2247e3b1fabc779f639d4326e; cross_origin_proto=SSL; WBStorage=4d96c54e|undefined; wb_view_log=1920*10801; WBtopGlobal_register_version=2023032721; crossidccode=CODE-gz-1PGMUh-186Bh0-dzKs5tyOcg3WiOR5b31d8; SSOLoginState=1679923752"
    }
    response = requests.get(url, headers=headers, cookies=cookies)
    response.encoding = response.apparent_encoding
    time.sleep(3)   # 加上3s 的延时防止被反爬
    return response.text


def get_string(text):
    t = ''
    flag = 1
    for i in text:
        if i == '<':
            flag = 0
        elif i == '>':
            flag = 1
        elif flag == 1:
            t += i
    return t


# 保存评论
def save_text_data(text_data):
    text_data = get_string(text_data)
    with open("data.csv", "a", encoding="utf-8", newline="")as fi:
        fi = csv.writer(fi)
        fi.writerow([text_data])


# 获取二级评论
def get_second_comments(cid):
    max_id = 0
    max_id_type = 0
    url = 'https://m.weibo.cn/comments/hotFlowChild?cid={}&max_id={}&max_id_type={}'
    while True:
        response = get_html(url.format(cid, max_id, max_id_type))
        content = json.loads(response)
        comments = content['data']
        for i in comments:
            text_data = i['text']
            save_text_data(text_data)
        max_id = content['max_id']
        max_id_type = content['max_id_type']
        if max_id == 0:		# 如果max_id==0表明评论已经抓取完毕了
            break


# 获取一级评论
def get_first_comments(mid):
    max_id = 0
    max_id_type = 0
    url = 'https://m.weibo.cn/comments/hotflow?id={}&mid={}&max_id={}&max_id_type={}'
    while True:
        response = get_html(url.format(mid, mid, max_id, max_id_type))
        content = json.loads(response)
        max_id = content['data']['max_id']
        max_id_type = content['data']['max_id_type']
        text_list = content['data']['data']
        for text in text_list:
            text_data = text['text']
            total_number = text['total_number']
            if int(total_number) != 0:  # 如果有二级评论就去获取二级评论。
                get_second_comments(text['id'])
            save_text_data(text_data)
        if int(max_id) == 0:    # 如果max_id==0表明评论已经抓取完毕了
            break


if __name__ == '__main__':
    """
    https://weibo.com//IAoPmpt5b#comment
    """
    mid = ["3850470588"]
    for id in mid:
        get_first_comments(id)    # 爬取一级评论