# coding:utf-8


import requests
import base64
import sys
import logging
import datetime
import time

# 在容器里运行时时间为 UTC 时间，不是北京时间，需要进行调整
def beijing(sec, what):
    beijing_time = datetime.datetime.now() + datetime.timedelta(hours=8)
    return beijing_time.timetuple()

def log_setting():
    """配置日志设置"""
    LOG_FILE_NAME = "log.log"
    LOG_PATH = LOG_FILE_NAME
    log_level = logging.INFO
    # 在容器里运行时时间为 UTC 时间，不是北京时间，需要进行调整
    logging.Formatter.converter = beijing
    logging.basicConfig(level=log_level,
                        format='[%(asctime)s] - [line:%(lineno)d] - %(levelname)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filename=LOG_PATH,
                        filemode='a')
    logger = logging.getLogger(__name__)
    logger.setLevel(log_level)
    return logger

def log_print(msg, level="info", to_log_file=True, to_console=True):
    """
    日志输出封装功能
    :param msg: 要输出的信息
    :param level: 日志级别，一般有 debug, info, warning, error, critical 等
    :param to_log_file: 是否保存到日志文件中
    :param to_console: 是否在控制台输出
    """
    if to_log_file:
        if level == 'debug':
            logger.debug(msg)
        elif level == 'info':
            logger.info(msg)
        elif level == 'warning':
            logger.warning(msg)
        elif level == 'error':
            logger.error(msg)
        elif level == 'critical':
            logger.critical(msg)
    if to_console:
        print(msg)

def hfgoSign(atpAuthToken, mobile, userId, userSig):
    cookies = {
        'atpAuthToken': atpAuthToken,
        'mobile': mobile,
        'userId': userId,
        'userSig': userSig,
    }

    headers = {
        'Host': 'atp.bol.wo.cn',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148       unicom{version:iphone_c@8.0904}{systemVersion:dis}{yw_code:}',
        'Accept-Language': 'zh-cn',
        'Referer': 'https://atp.bol.wo.cn/atpsign/ACT202012221038331042965g65tNa?product=hfgo',
    }

    params = (
        ('actId', '1516'),
    )
    surl = b'aHR0cHM6Ly9hdHAuYm9sLndvLmNuL2F0cGFwaS9hY3QvYWN0VXNlclNpZ24vZXZlcnlkYXlTaWdu'
    url = base64.b64decode( surl ).decode()
    response = requests.get(url, headers=headers, params=params, cookies=cookies)
    print(response.text)
    # log_print("话费够：" + response.text)

def sljsign0883(acw_tc, sign):
    time_369 = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.localtime())

    cookies = {
        'acw_tc': acw_tc,
    }

    headers = {
        'Host': 'api.369cx.cn',
        'accept': '*/*',
        'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6IiIsInJvbGUiOiJWaXNpdG9yLFVzZXIiLCJuYW1laWQiOiI4NzEyODkiLCJqdGkiOiIyMDRkZDI0YS05ZTY3LTQzYmUtYjQ0Yi1jYzBmZjk3MWM1ZDciLCJuYmYiOjE2NDEzMDM0NDEsImV4cCI6MTY0Mzg5NTQ0MSwiaWF0IjoxNjQxMzAzNDQxLCJpc3MiOiJ3ZWIuMzY5Y3guY24iLCJhdWQiOiJhcGkud2ViLjM2OWN4LmNuIn0.AV0iGHMfK7CYNNYW2KzWVJb9IjTXtpYL3AJ5fNeKT5GRgg5_5q918bEQbsVYG1Jm_qw86Jn3IjqJvOnOl6AFkLsq_-88hjjUW1qGlBwtWokSteWxDso77JdQl54o413lE9atCvgZuZq-cYxmgmW4Y_1Fi7yBdgEYdYrgAIGsU7-QiGeQyAquASuUeYl30reovHPeXaiU4BlqdlTrmmdVujq9The-Nk0rU7lrsNZtcGMJBEb0RKKwrLiIFRcf_7gwTSRswCIgL_u3mDLpbTzVZZrqZJorRmb0gybNaeCMxL8Z6_Q5PxKJaS546yFY_Wq3gAJ9gPPv5Lg8HkY5EgNf7A',
        'accept-language': 'zh-Hans-CN;q=1, en-CN;q=0.9',
        'date': time_369,
        'cityid': '2500',
        'geo': 'F%c..Vy',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X; iPhone_SE) Cx369iOS/7100 NetType/WIFI DarkMode/1 BlindMode/0',
        'sign': sign,
    }

    surl = b'aHR0cHM6Ly9hcGkuMzY5Y3guY24vdjIvSW50ZWdyYWwvRGF5bHlTaWdu'
    url = base64.b64decode( surl ).decode()
    response = requests.get(url, headers=headers, cookies=cookies)
    print(response.text)

def sljsign7207(sign_7207, auth_7207):
    time_369 = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.localtime())
    headers = {
        'Host': 'api.369cx.cn',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Xiaomi/Redmi 4) Cx369Android/7100 NetType/WIFI BusQrCodeSdkVersion/4 DarkMode/0 CityId/2500',
        'authorization': auth_7207,
        'sign': sign_7207,
        'cityid': '2500',
        'date': time_369,
        'accept-encoding': 'gzip',
    }
    surl = b'aHR0cHM6Ly9hcGkuMzY5Y3guY24vdjIvSW50ZWdyYWwvRGF5bHlTaWdu'
    url = base64.b64decode( surl ).decode()
    response = requests.get(url, headers=headers)
    print(response.text)

def sljsign8291(sign_8291):
    time_369 = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.localtime())
    headers = {
        'Host': 'api.369cx.cn',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Xiaomi/Redmi 4) Cx369Android/7100 NetType/WIFI BusQrCodeSdkVersion/4 DarkMode/0 CityId/2500',
        'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6IiIsInJvbGUiOiJWaXNpdG9yLFVzZXIiLCJuYW1laWQiOiIxMDY0NzI2IiwianRpIjoiYjI0OWFlOTMtMWFhOS00ZGU0LTkzOTQtYTczYjc4YzRjMGZlIiwibmJmIjoxNjQxNjExODU4LCJleHAiOjE2NDQyMDM4NTgsImlhdCI6MTY0MTYxMTg1OCwiaXNzIjoid2ViLjM2OWN4LmNuIiwiYXVkIjoiYXBpLndlYi4zNjljeC5jbiJ9.Z_KHASsbjTK6zqFbJYfw_ji2-cUuewiYFfSJ4jPHbQfpx2j2fenYPgxIx_2ZNIYJaTuugw2M3IPSVaRyr-WnIuwoMIrcWtuTJaJ6NkneGpesp37Qb4OuOviViY8y8PYlXWnja6Un8Ebdb_opGRVI6VBgzuZ7Uev7b1rvxI1q8UhHO8pC2KT_oM5fOY1FI2s8XJO9PcM3sx9_YxyKygzJSHcHeGd7B3ct4y2iDrCgbAKXKIt8nXu2oVniJgX4kHFI3oih871WfP9GPmIElieitlD_zSmdf5fBqKJ96q5fucLivz74nhh0zGp0u30fLtzbgDrdeRh1XWS5egxBV5J0CA',
        'sign': sign_8291,
        'cityid': '2500',
        'date': time_369,
        'accept-encoding': 'gzip',
    }
    surl = b'aHR0cHM6Ly9hcGkuMzY5Y3guY24vdjIvSW50ZWdyYWwvRGF5bHlTaWdu'
    url = base64.b64decode( surl ).decode()
    response = requests.get(url, headers=headers)
    print(response.text)

def yhsign(memberid, access_token, deviceid, sign):
    time_yh = int(round(time.time() * 1000))
    headers = {
        'Host': 'api.yonghuivip.com',
        'Content-Type': 'application/json',
        'Origin': 'https://m.yonghuivip.com',
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 YhStore/7.12.1(client/phone; iOS 14.6; iPhone8,4)',
        'Referer': 'https://m.yonghuivip.com/yh-m-site/yh-point-exchange/index.html?needlocation=1&canShare=0',
        'Accept-Language': 'zh-cn',
    }

    params = (
        ('timestamp', time_yh),
        ('channel', 'ios'),
        ('platform', 'ios'),
        ('v', '7.12.1.2'),
        ('app_version', '7.12.1.2'),
        ('sellerid', ''),
        ('channelSub', ''),
        ('brand', 'iPhone'),
        ('model', 'iPhone SE (A1662/A1723/A1724)'),
        ('os', 'ios'),
        ('osVersion', '14.6'),
        ('networkType', '4G'),
        ('screen', '320*568'),
        ('productLine', 'YhStore'),
        ('appType', 'h5'),
        ('deviceid', deviceid),
        ('shopid', '95DC'),
        ('memberid', memberid),
        ('access_token', access_token),
        ('sign', sign),
    )

    data = '{"memberId":"' + memberid + '","shopId":"95DC","missionid":39}'
    yhhost = 'yonghuivip'
    response = requests.post('https://api.' + yhhost + '.com/web/coupon/signreward/sign', headers=headers, params=params, data=data)
    print(response.text)

if __name__ == '__main__':
    # 日志配置
    logger = log_setting()

    if len(sys.argv) != 14:
        raise Exception("传入参数不正确！")

    atpAuthToken = sys.argv[1]
    mobile = sys.argv[2]
    userId = sys.argv[3]
    userSig = sys.argv[4]

    acw_tc = sys.argv[5]
    sign1 = sys.argv[6]

    sign_7207 = sys.argv[7]
    sign_8291 = sys.argv[8]

    memberid = sys.argv[9]
    access_token = sys.argv[10]
    deviceid = sys.argv[11]
    sign = sys.argv[12]

    auth_7207 = sys.argv[13]

    # 话费够
    # hfgoSign(atpAuthToken, mobile, userId, userSig)
    # 公交

    sljsign7207(sign_7207, auth_7207)
    # sljsign8291(sign_8291)
    # sljsign0883(acw_tc, sign1)
    # yhsign(memberid, access_token, deviceid, sign)
