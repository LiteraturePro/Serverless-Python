# -*- coding: utf8 -*-
import requests
'''
-包含邮局120朵,6项签到，每日抽奖及签到7日抽奖
-sckey-    Server酱SCKEY
-Cookie-   Cookie
'''

sckey = ''
Cookie = ''


uid = Cookie.split("; ")
t_uUid = ''
for i in uid:
    if i.find('uid=') >= 0:
        t_uUid = i.split('=')[1]
Url_a = 'https://node.kg.qq.com/webapp/proxy?ns=proto_profile&cmd=profile.getProfile&mapExt=JTdCJTIyZmlsZSUyMiUzQSUyMnByb2ZpbGVfd2ViYXBwSmNlJTIyJTJDJTIyY21kTmFtZSUyMiUzQSUyMlByb2ZpbGVHZXQlMjIlMkMlMjJhcHBpZCUyMiUzQTEwMDA2MjYlMkMlMjJkY2FwaSUyMiUzQSU3QiUyMmludGVyZmFjZUlkJTIyJTNBMjA1MzU5NTk3JTdEJTJDJTIybDVhcGklMjIlM0ElN0IlMjJtb2RpZCUyMiUzQTI5NDAxNyUyQyUyMmNtZCUyMiUzQTI2MjE0NCU3RCUyQyUyMmlwJTIyJTNBJTIyMTAwLjExMy4xNjIuMTc4JTIyJTJDJTIycG9ydCUyMiUzQSUyMjEyNDA2JTIyJTdE&t_uUid=' + t_uUid
Url_b = 'https://node.kg.qq.com/webapp/proxy?ns=KG_TASK&cmd=task.getLottery&ns_inbuf=&mapExt=JTdCJTIyZmlsZSUyMiUzQSUyMnRhc2tKY2UlMjIlMkMlMjJjbWROYW1lJTIyJTNBJTIyTG90dGVyeVJlcSUyMiUyQyUyMnduc0NvbmZpZyUyMiUzQSU3QiUyMmFwcGlkJTIyJTNBMTAwMDU1NyU3RCUyQyUyMmw1YXBpJTIyJTNBJTdCJTIybW9kaWQlMjIlM0E1MDM5MzclMkMlMjJjbWQlMjIlM0E1ODk4MjQlN0QlN0Q%3D&t_uid=' + t_uUid + '&t_iShowEntry=1&t_type='
t_type = ['1','2']
Url_e = 'https://node.kg.qq.com/webapp/proxy?ns=KG_TASK&cmd=task.getLottery&mapExt=JTdCJTIyZmlsZSUyMiUzQSUyMnRhc2tKY2UlMjIlMkMlMjJjbWROYW1lJTIyJTNBJTIyTG90dGVyeVJlcSUyMiUyQyUyMmw1YXBpJTIyJTNBJTdCJTIybW9kaWQlMjIlM0E1MDM5MzclMkMlMjJjbWQlMjIlM0E1ODk4MjQlN0QlMkMlMjJsNWFwaV9leHAxJTIyJTNBJTdCJTIybW9kaWQlMjIlM0E4MTcwODklMkMlMjJjbWQlMjIlM0EzODAxMDg4JTdEJTdE&t_uid=' + t_uUid + '&t_type=103'

Url_c = 'https://node.kg.qq.com/webapp/proxy?ns=KG_TASK&cmd=task.signinGetAward&mapExt=JTdCJTIyZmlsZSUyMiUzQSUyMnRhc2tKY2UlMjIlMkMlMjJjbWROYW1lJTIyJTNBJTIyR2V0U2lnbkluQXdhcmRSZXElMjIlMkMlMjJ3bnNDb25maWclMjIlM0ElN0IlMjJhcHBpZCUyMiUzQTEwMDA2MjYlN0QlMkMlMjJsNWFwaSUyMiUzQSU3QiUyMm1vZGlkJTIyJTNBNTAzOTM3JTJDJTIyY21kJTIyJTNBNTg5ODI0JTdEJTdE&t_uid=' + t_uUid + '&t_iShowEntry='
t_iShowEntry =['1','2','4','16','128','512']
Url_d = 'https://node.kg.qq.com/webapp/proxy?ns=KG_TASK&cmd=task.getLottery&mapExt=JTdCJTIyZmlsZSUyMiUzQSUyMnRhc2tKY2UlMjIlMkMlMjJjbWROYW1lJTIyJTNBJTIyTG90dGVyeVJlcSUyMiUyQyUyMnduc0NvbmZpZyUyMiUzQSU3QiUyMmFwcGlkJTIyJTNBMTAwMDU1NyU3RCUyQyUyMmw1YXBpJTIyJTNBJTdCJTIybW9kaWQlMjIlM0E1MDM5MzclMkMlMjJjbWQlMjIlM0E1ODk4MjQlN0QlN0Q&t_uid=' + t_uUid + '&t_iShowEntry=4&t_type=104'
Url_1 = 'https://node.kg.qq.com/webapp/proxy?ns=proto_music_station&cmd=message.batch_get_music_cards&mapExt=JTdCJTIyY21kTmFtZSUyMiUzQSUyMkdldEJhdGNoTXVzaWNDYXJkc1JlcSUyMiUyQyUyMmZpbGUlMjIlM0ElMjJwcm90b19tdXNpY19zdGF0aW9uSmNlJTIyJTJDJTIyd25zRGlzcGF0Y2hlciUyMiUzQXRydWUlN0Q&t_uUid=' + t_uUid + '&g_tk_openkey='
Url_2 = 'https://node.kg.qq.com/webapp/proxy?t_stReward%3Aobject=%7B%22uInteractiveType%22%3A1%2C%22uRewardType%22%3A0%2C%22uFlowerNum%22%3A15%7D&ns=proto_music_station&cmd=message.get_reward&mapExt=JTdCJTIyY21kTmFtZSUyMiUzQSUyMkdldFJld2FyZFJlcSUyMiUyQyUyMmZpbGUlMjIlM0ElMjJwcm90b19tdXNpY19zdGF0aW9uSmNlJTIyJTJDJTIyd25zRGlzcGF0Y2hlciUyMiUzQXRydWUlN0Q&t_uUid=' + t_uUid + '&t_strUgcId='
Url_3 = 'https://node.kg.qq.com/webapp/proxy?t_stReward%3Aobject=%7B%22uInteractiveType%22%3A0%2C%22uRewardType%22%3A0%2C%22uFlowerNum%22%3A10%7D&ns=proto_music_station&cmd=message.get_reward&mapExt=JTdCJTIyY21kTmFtZSUyMiUzQSUyMkdldFJld2FyZFJlcSUyMiUyQyUyMmZpbGUlMjIlM0ElMjJwcm90b19tdXNpY19zdGF0aW9uSmNlJTIyJTJDJTIyd25zRGlzcGF0Y2hlciUyMiUzQXRydWUlN0Q&t_uUid=' + t_uUid + '&t_strUgcId='

def run():
    try:
        res_1 = requests.get(Url_a, headers={'Cookie': Cookie})
        num_a = res_1.json()['data']['profile.getProfile']['uFlowerNum']
        for index, T_iShowEntry in enumerate(t_iShowEntry):
            res_b = requests.get(Url_c + T_iShowEntry, headers={'Cookie': Cookie})
        for index, T_type in enumerate(t_type):
            res_a = requests.get(Url_b + T_type, headers={'Cookie': Cookie})
        for g_tk_openkey in range(16):
            res_2 = requests.get(Url_1 + str(g_tk_openkey), headers={'Cookie': Cookie})
            vctMusicCards = res_2.json()['data']['message.batch_get_music_cards']['vctMusicCards']
            List = sorted(vctMusicCards,key=lambda x: x['stReward']['uFlowerNum'],reverse=True)[0]
            strUgcId = List['strUgcId']
            strKey = List['strKey']
            Url = strUgcId + '&t_strKey=' + strKey
            if List['stReward']['uFlowerNum'] > 10:
                res_3 = requests.get(Url_2 + Url, headers={'Cookie': Cookie})
            else:
                if List['stReward']['uFlowerNum'] > 1:
                    res_3 = requests.get(Url_3 + Url, headers={'Cookie': Cookie})
        res_f = requests.get(Url_d, headers={'Cookie': Cookie})
        res_d = requests.get(Url_e, headers={'Cookie': Cookie})
        res_4 = requests.get(Url_a, headers={'Cookie': Cookie})
        num_b = res_4.json()['data']['profile.getProfile']['uFlowerNum']
        num_c = int(num_b)-int(num_a)
        if num_c == 0:
            num = '请不要重复领取哦.....当前账户为' + str(num_b) + '朵鲜花！'
        else:
            num = '本次成功领取' + str(num_c) + '朵鲜花！'
    except:
        num = 'Cookie效验失败'
    requests.get('https://sc.ftqq.com/' + sckey + '.send?text=全民K歌签到通知&desp=' + num)
    print(num)

def main_handler(event, context):
    run()