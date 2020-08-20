# -*- coding: utf8 -*-
# -*- coding: utf8 -*-
from requests import Session
from time import sleep
from random import randint
import requests

sckey = ''

def main2(*args):
    sleep(randint(0, 10))
    # 数据
    like_url = 'https://tieba.baidu.com/mo/q/newmoindex?'
    sign_url = 'http://tieba.baidu.com/sign/add'
    tbs = '4fb45fea4498360d1547435295'
    head = {
        'Accept': 'text/html, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Cookie': 'BDUSS=WxVT0FzZn5JYUNHan5YR2FYUHZDRnp1MThqVHdGN2ZpVEM1bnUxR1VJaDd0RWhmRVFBQUFBJCQAAAAAAAAAAAEAAABdKY860e7OxND91NrCt8nPAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHsnIV97JyFfb; BDUSS_BFESS=WxVT0FzZn5JYUNHan5YR2FYUHZDRnp1MThqVHdGN2ZpVEM1bnUxR1VJaDd0RWhmRVFBQUFBJCQAAAAAAAAAAAEAAABdKY860e7OxND91NrCt8nPAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHsnIV97JyFfb;STOKEN=d38e3183bf24cfb2e40cdb6649c5fc6032097d0a3598a1ded5d3ed54c18ea602',
        'Host': 'tieba.baidu.com',
        'Referer': 'http://tieba.baidu.com/i/i/forum',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/71.0.3578.98 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'}
    s = Session()
 
 
    # 获取关注的贴吧
    bars = []
    dic = s.get(like_url, headers=head).json()['data']['like_forum']
    for bar_info in dic:
        bars.append(bar_info['forum_name'])
 
 
    # 签到
    already_signed_code = 1101
    success_code = 0
    need_verify_code = 2150040
    already_signed = 0
    succees = 0
    failed_bar = []
    n = 0
    sleep(randint(0, 10))
 
    while n < len(bars):
        sleep(0.5)
        bar = bars[n]
        data = {
            'ie': 'utf-8',
            'kw': bar,
            'tbs': tbs
        }
        try:
            r = s.post(sign_url, data=data, headers=head)
        except Exception as e:
            print(f'未能签到{bar}, 由于{e}。')
            failed_bar.append(bar)
            continue
        dic = r.json()
        msg = dic['no']
        if msg == already_signed_code: already_signed += 1; r = '已经签到过了!'
        elif msg == need_verify_code: n -= 1; r = '需要验证码，即将重试!'
        elif msg == success_code: r = f"签到成功!你是第{dic['data']['uinfo']['user_sign_rank']}个签到的吧友,共签到{dic['data']['uinfo']['total_sign_num']}天。"
        else: r = '未知错误!' + dic['error']
        print(f"{bar}：{r}")
        succees += 1
        n += 1
    l = len(bars)
    failed = "\n失败列表："+'\n'.join(failed_bar) if len(failed_bar) else ''
    bai=f'''共{l}个吧，其中: {succees}个吧签到成功，{len(failed_bar)}个吧签到失败，{already_signed}个吧已经签到。{failed}'''
    print(f'''共{l}个吧，其中: {succees}个吧签到成功，{len(failed_bar)}个吧签到失败，{already_signed}个吧已经签到。{failed}''')
    requests.get('https://sc.ftqq.com/' + sckey + '.send?text=百度贴吧签到通知&desp=' + bai)
def main_handler(event, context):
    main2()