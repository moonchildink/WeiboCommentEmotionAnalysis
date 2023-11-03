def zhihu_comment(url):
    content = requests.get(url, headers=headers)
    dick = json.loads(content.content)
    comment_list = []
    for data in dick['data']:
        comment_list.append(data['content'])
        for child_comment in data['child_comments']:
            comment_list.append(child_comment['content'])


    while not dick['paging']['is_end']:
        next_url = dick['paging']['next']
        dick = json.loads(requests.get(next_url, headers=headers).content)
        for data in dick['data']:
            comment_list.append(data['content'])
            for child_comment in data['child_comments']:
                comment_list.append(child_comment['content'])

    return comment_list

li = zhihu_comment(r'https://www.zhihu.com/api/v4/comment_v5/answers/2649393382/root_comment?order_by=score&limit=20&offset=')


with open('zhihu.txt','w',encoding='utf-8') as f:
    for i in li:
        f.write(i+'\n')