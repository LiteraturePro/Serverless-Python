# -*- coding: utf8 -*-
#本项目不建议使用server酱，因为不够直观
import requests, json
import time

spkey = ''          #CoolPush酷推
def get_iciba_everyday():
    icbapi = 'http://open.iciba.com/dsapi/'
    eed = requests.get(icbapi)
    bee = eed.json()               #返回的数据
    english = eed.json()['content']
    zh_CN = eed.json()['note']
    str = '\n【奇怪的知识】\n' + english + '\n' + zh_CN
    return str

# print(get_iciba_everyday())

def main(*args):
    api = 'http://t.weather.itboy.net/api/weather/city/'             #API地址，必须配合城市代码使用
    city_code = '101260406'               #进入https://where.heweather.com/index.html查询你的城市代码
    tqurl = api + city_code
    response = requests.get(tqurl)
    d = response.json()         #将数据以json形式返回，这个d就是返回的json数据
    print(d)
    
    if(d['status'] == 200):     #当返回状态码为200，输出天气状况
        print("城市：",d["cityInfo"]["parent"], d["cityInfo"]["city"])
        print("更新时间：",d["time"])
        print("日期：",d["data"]["forecast"][0]["ymd"])
        print("星期：",d["data"]["forecast"][0]["week"])
        print("天气：",d["data"]["forecast"][0]["type"])
        print("温度：",d["data"]["forecast"][0]["high"],d["data"]["forecast"][0]["low"])
        print("湿度：",d["data"]["shidu"])
        print("PM25:",d["data"]["pm25"])
        print("PM10:",d["data"]["pm10"])
        print("空气质量：",d["data"]["quality"])
        print("风力风向：",d["data"]["forecast"][0]["fx"],d["data"]["forecast"][0]["fl"])
        print("感冒指数：",d["data"]["ganmao"])
        print("温馨提示：",d["data"]["forecast"][0]["notice"],"。")

        cpurl = 'https://push.xuthus.cc/send/'+spkey               #自己改发送方式，我专门创建了个群来收消息，所以我用的group
        tdwt = '【今日天气】\n城市：'+d['cityInfo']['parent']+' '+d['cityInfo']['city']+'\n日期：'+d["data"]["forecast"][0]["ymd"]+'\n星期：'+d["data"]["forecast"][0]["week"]+'\n天气：'+d["data"]["forecast"][0]["type"]+'\n温度：'+d["data"]["forecast"][0]["high"]+' '+d["data"]["forecast"][0]["low"]+'\n湿度：'+d["data"]["shidu"]+'\n空气质量：'+d["data"]["quality"]+'\n风力风向：'+d["data"]["forecast"][0]["fx"]+' '+d["data"]["forecast"][0]["fl"]+'\n温馨提示：'+d["data"]["forecast"][0]["notice"]+'。\n[Time：'+d["time"]+']\n'         #天气提示内容，基本上该有的都做好了，如果要添加信息可以看上面的print，我感觉有用的我都弄进来了。
        requests.post(cpurl,tdwt.encode('utf-8'))         #把天气数据转换成UTF-8格式，不然要报错。
    else:
        error = '【出现错误】\n　　今日天气推送错误，请检查服务状态！'
        requests.post(cpurl,error.encode('utf-8'))

def main_handler(event, context):
    return main()

if __name__ == '__main__':
    main()