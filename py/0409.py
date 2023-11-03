import json
import requests

headers = {
    'User=Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
    'Cookie':'PC_TOKEN=de15cf9de8; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW.ah1ZCkrZli1KX4braBpx5JpX5KzhUgL.Fo-4eK54eh.ReKe2dJLoI7f_dcvVqcyDdsBEehz7; WBPSESS=Q4mocWB9j3toNvru27wa1TepLPXtAnu2XAXlhijHDmRDo3c7fhos1X1YsQ5sCQmRNcVN9W4HihTP2x1ITr_j-_bW93ayUrSLA82jgoc18sP1EvFZtdCP_1y9FluueQF5vY73jyYNeLx9uHFkOiAdvQ==; SINAGLOBAL=2129311165616.0813.1669013358502; ULV=1669013911487:2:2:2:5684428808012.402.1669013911365:1669013358503; ALF=1700549732; SUB=_2A25Of1C2DeRhGeNH6lIY8CfEyj-IHXVtDcV-rDV8PUNbmtAfLRTWkW9NSsnp9C-go4Q2I-P2WKyciynFznYmW2Ve; SSOLoginState=1669013734; XSRF-TOKEN=11QMGfwtyRXSFeqt4EtiCVXV; _s_tentry=weibo.com; Apache=5684428808012.402.1669013911365'
}
bilibili_cookie = r"buvid3=24F31FD6-220B-2314-1791-29B4B19101ED38432infoc; b_nut=1673523238; i-wanna-go-back=-1; b_ut=5; _uuid=4A17E755-4E4A-FC3F-10F3F-6DC2CD56746439320infoc; buvid_fp=7e77a1e02fb82712142f58f8bf266314; buvid4=75762ED4-0F59-F6E5-CC13-AF2D0A78746839991-023011219-Yy4vm8XQ%2BSYNBA%2FUziFw6g%3D%3D; fingerprint=08c90d6be64a7cd26d231ad186351599; buvid_fp_plain=undefined; SESSDATA=9494fbc9%2C1689075608%2C7bd24%2A11; bili_jct=3086cea8aed34ae2abe38fd23845c678; DedeUserID=203460504; DedeUserID__ckMd5=79d56fdab8baf61b; nostalgia_conf=-1; CURRENT_FNVAL=4048; rpdid=|(u))u~)uRJJ0J'uY~JlkJYJR; PVID=1; LIVE_BUVID=AUTO8416761100285718; header_theme_version=CLOSE; home_feed_column=5; bp_video_offset_203460504=778836669434429400; CURRENT_PID=49587320-d2f4-11ed-84e7-0d474b46558f; b_lsid=10FE652FA_18764615EA2; share_source_origin=QQ; bsource=share_source_qqchat; sid=5q9k8s03"


bilibili_url = r"https://api.bilibili.com/x/v2/reply/main?csrf=3086cea8aed34ae2abe38fd23845c678&mode=3&next=0&oid=936714657&plat=1&seek_rpid=&type=1"

res = requests.get(bilibili_url,headers = headers)

dic = json.loads(res.content)

comment_list = []

for reply in dic['data']['replies']:
    comment_list.append(reply['content']['message'])
    if reply['replies'] is not None:
        for replyss in reply['replies']:
            comment_list.append(replyss['content']['message'])

print(len(comment_list))


