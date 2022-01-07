# coding:utf-8


import requests
import base64
import sys
import logging
import datetime

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
    log_print("话费够：" + response.text)

def sljsign(acw_tc, sign):

    cookies = {
        'acw_tc': acw_tc,
    }

    headers = {
        'Host': 'api.369cx.cn',
        'accept': '*/*',
        'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6IiIsInJvbGUiOiJWaXNpdG9yLFVzZXIiLCJuYW1laWQiOiI4NzEyODkiLCJqdGkiOiIyMDRkZDI0YS05ZTY3LTQzYmUtYjQ0Yi1jYzBmZjk3MWM1ZDciLCJuYmYiOjE2NDEzMDM0NDEsImV4cCI6MTY0Mzg5NTQ0MSwiaWF0IjoxNjQxMzAzNDQxLCJpc3MiOiJ3ZWIuMzY5Y3guY24iLCJhdWQiOiJhcGkud2ViLjM2OWN4LmNuIn0.AV0iGHMfK7CYNNYW2KzWVJb9IjTXtpYL3AJ5fNeKT5GRgg5_5q918bEQbsVYG1Jm_qw86Jn3IjqJvOnOl6AFkLsq_-88hjjUW1qGlBwtWokSteWxDso77JdQl54o413lE9atCvgZuZq-cYxmgmW4Y_1Fi7yBdgEYdYrgAIGsU7-QiGeQyAquASuUeYl30reovHPeXaiU4BlqdlTrmmdVujq9The-Nk0rU7lrsNZtcGMJBEb0RKKwrLiIFRcf_7gwTSRswCIgL_u3mDLpbTzVZZrqZJorRmb0gybNaeCMxL8Z6_Q5PxKJaS546yFY_Wq3gAJ9gPPv5Lg8HkY5EgNf7A',
        'accept-language': 'zh-Hans-CN;q=1, en-CN;q=0.9',
        'date': 'Fri, 07 Jan 2022 11:22:42 GMT',
        'cityid': '2500',
        'geo': 'F%c..Vy',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X; iPhone_SE) Cx369iOS/7100 NetType/WIFI DarkMode/1 BlindMode/0',
        'sign': sign,
    }

    surl = b'aHR0cHM6Ly9hcGkuMzY5Y3guY24vdjIvSW50ZWdyYWwvRGF5bHlTaWdu'
    url = base64.b64decode( surl ).decode()
    response = requests.get(url, headers=headers, cookies=cookies)
    print(response.text)
    log_print("公交：" + response.text)

if __name__ == '__main__':
    # 日志配置
    logger = log_setting()

    if len(sys.argv) != 7:
        raise Exception("传入参数不正确！")

    atpAuthToken = sys.argv[1]
    mobile = sys.argv[2]
    userId = sys.argv[3]
    userSig = sys.argv[4]

    acw_tc = sys.argv[5]
    sign1 = sys.argv[6]

    # 话费够
    hfgoSign(atpAuthToken, mobile, userId, userSig)
    # 公交
    sljsign(acw_tc, sign1)
