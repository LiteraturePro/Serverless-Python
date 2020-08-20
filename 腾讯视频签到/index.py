# coding: utf-8
'''
@author: sy-records
@license: https://github.com/sy-records/v-checkin/blob/master/LICENSE
@contact: 52o@qq52o.cn
@desc: 腾讯视频好莱坞会员V力值签到，支持两次签到：一次正常签到，一次手机签到。
@blog: https://qq52o.me
'''

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests

auth_refresh_url = 'https://access.video.qq.com/user/auth_refresh?vappid=11059694&vsecret=fdf61a6be0aad57132bc5cdf78ac30145b6cd2c1470b0cfe&type=qq&g_tk=436137217&g_vstk=1103305739&g_actk=1233618242&callback=jQuery19107078619711839995_1596257528721&_=1596257528722'
sckey = 'SCU107437T845b42e2ad9cd989053b83d77bdf64e85f1fabb4cc842'


ftqq_url = "https://sc.ftqq.com/%s.send"%(sckey)
url1 = 'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=hierarchical_task_system&cmd=2'
url2 = 'https://v.qq.com/x/bu/mobile_checkin'

login_headers = {
    'Referer': 'https://v.qq.com',
    'Cookie': 'pgv_pvi=6428140544; RK=VJ5QDBTi6z; ptcz=5d8ebf03fd2e31b8d366148ba5ade33a6ddbf9198d7df99b9ae627a4e7efc6be; tvfe_boss_uuid=c4686e3a97ba60f2; video_guid=ac235aeb387f37d7; video_platform=2; pgv_pvid=6710598928; main_login=qq; vqq_access_token=395B903E37FB32B9BC8E4D90937EBD2D; vqq_appid=101483052; vqq_openid=480311F122A6383EE0A38475A0B0B486; vqq_vuserid=171165010; vqq_refresh_token=116C6E3473E5BD5655393E13C2961605; uin=o2440229611; pgv_info=ssid=s6998905652; skey=@OB0v8MMBQ; vqq_vusession=XFu68M-ifNbvTtuzppX1cw..; o_cookie=2440229611; uid=228756450; pgv_si=s6600956928; _qpsvr_localtk=0.00432450409112195; vqq_next_refresh_time=6227; vqq_login_time_init=1596256906; login_time_last=2020-8-1 12:41:48'
}

login = requests.get(auth_refresh_url, headers=login_headers)
cookie = requests.utils.dict_from_cookiejar(login.cookies)

if not cookie:
    print ("auth_refresh error")
    payload = {'text': '腾讯视频V力值签到通知', 'desp': '获取Cookie失败，Cookie失效'}
    requests.post(ftqq_url, params=payload)

sign_headers = {
    'Cookie': 'pgv_pvi=6428140544; RK=VJ5QDBTi6z; ptcz=5d8ebf03fd2e31b8d366148ba5ade33a6ddbf9198d7df99b9ae627a4e7efc6be; tvfe_boss_uuid=c4686e3a97ba60f2; video_guid=ac235aeb387f37d7; video_platform=2; pgv_pvid=6710598928; main_login=qq; vqq_access_token=395B903E37FB32B9BC8E4D90937EBD2D; vqq_appid=101483052; vqq_openid=480311F122A6383EE0A38475A0B0B486; vqq_vuserid=171165010; vqq_refresh_token=116C6E3473E5BD5655393E13C2961605; uin=o2440229611; pgv_info=ssid=s6998905652; skey=@OB0v8MMBQ; o_cookie=2440229611; uid=228756450; pgv_si=s6600956928; _qpsvr_localtk=0.00432450409112195; vqq_next_refresh_time=6227; vqq_login_time_init=1596256906; login_time_last=2020-8-1 12:41:48; vqq_vusession=' + cookie['vqq_vusession'] + ';',
    'Referer': 'https://m.v.qq.com'
}
def start():
    sign1 = requests.get(url1,headers=sign_headers).text
    if 'Account Verify Error' in sign1:
        print ('Sign1 error,Cookie Invalid')
        status = "链接1 失败，Cookie失效"
    else:
        print ('Sign1 Success')
        status = "链接1 成功，获得V力值：" + sign1[42:-14]

    sign2 = requests.get(url2,headers=sign_headers).text
    if 'Unauthorized' in sign2:
        print ('Sign2 error,Cookie Invalid')
        status = status + "\n\n 链接2 失败，Cookie失效"
    else:
        print ('Sign2 Success')
        status = status + "\n\n 链接2 成功"

    payload = {'text': '腾讯视频V力值签到通知', 'desp': status}
    requests.post(ftqq_url, params=payload)

def main_handler(event, context):
    return start()
if __name__ == '__main__':
    start()