# coding:utf-8


import requests
import base64
import sys
import logging
from datetime import datetime
import time
from datetime import timedelta
from datetime import timezone


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



def sljsign7207(sign_7207):
    time_369 = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.localtime())
    headers = {
        'Host': 'api.369cx.cn',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Xiaomi/Redmi 4) Cx369Android/7100 NetType/WIFI BusQrCodeSdkVersion/4 DarkMode/0 CityId/2500',
        'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6IiIsInJvbGUiOiJWaXNpdG9yLFVzZXIiLCJuYW1laWQiOiIxMDY0NjY5IiwianRpIjoiMTMzYWQ3MzItOTZmYy00ZTM2LTgxZmYtYmI5OWJkNWE0NGQ0IiwibmJmIjoxNjQxNjA4NDA3LCJleHAiOjE2NDQyMDA0MDcsImlhdCI6MTY0MTYwODQwNywiaXNzIjoid2ViLjM2OWN4LmNuIiwiYXVkIjoiYXBpLndlYi4zNjljeC5jbiJ9.hJwcS9kfprgVISDYQLIsfdd2yC9SJKdU5-uz4ai23qcV6C7cbUSvxUzJchG7KquelXe6-VejD6FivrrDVuRX0ZnAGKq9QZ1rvT6F9qUe_JfEEncFbsveZ71hI3cIfeDXKpwd9cdI0Mtgj5vmfpMfM-MzLBZciG_dZSK_gaCR-62S5ohYm0ZWCCU8p_CV6jnaX3J10OxoyBhwUPa1rKVO_MLLQ72bOWdMfSlJagtHDYT62Azq2MiGg_uWMQnHbn8BMGFwNVcOScKTMXJgRwex-LumLZS4i4z-13kt-SdHZjJVj6hl5FYgBWVO5f2jfYRzmEkPyI8MN1O_RVUEBVmDAw',
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
    
def sljsign8958(sign_8958):
    time_369 = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.localtime())
    headers = {
        'Host': 'api.369cx.cn',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Xiaomi/Redmi 4) Cx369Android/7200 NetType/WIFI BusQrCodeSdkVersion/4 DarkMode/0 CityId/2500',
        'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6IiIsInJvbGUiOiJWaXNpdG9yLFVzZXIiLCJuYW1laWQiOiIxMDg3Nzk1IiwianRpIjoiODA5NDc3NjgtNjhlNy00ZWVkLTg3ZDctOWUxODkxM2Q5Y2EyIiwibmJmIjoxNjQ0MTU4OTgwLCJleHAiOjE2NDY3NTA5ODAsImlhdCI6MTY0NDE1ODk4MCwiaXNzIjoid2ViLjM2OWN4LmNuIiwiYXVkIjoiYXBpLndlYi4zNjljeC5jbiJ9.jDfeuy805nDOFa1liyf38L1TCeZjg1TiL59s6qx6Su4RKKcyKJkZYUFdnd4ul--zoxsHKakW5LTqH5YODh2Rc-UN-FsUmj4xW1Yw1GugHF1F5rnzEFUHE7h4tuy6VzHfYaHnQxo1yHJgNoszq-2NKmbbBWuuICiIZUd6bv0nPzRe_BCCqFqy4o5zg2HBDGrxo_xWRkB3MaeWhKmNBMk8EuJLoscT9wQJ8l4dhEuW_Y-GVAu-SccQlkwjwRbnHkhLxx0gGMXNaUCcbKNLE7rNBMA5DpAXxuCmD5N-PmYile4yRNDjYMVJStmwooIln72cf2zEIgbN4_vj446mZ9bSxQ',
        'sign': sign_8958,
        'cityid': '2500',
        'date': time_369,
        'accept-encoding': 'gzip',
    }
    surl = b'aHR0cHM6Ly9hcGkuMzY5Y3guY24vdjIvSW50ZWdyYWwvRGF5bHlTaWdu'
    url = base64.b64decode( surl ).decode()
    response = requests.get(url, headers=headers)
    print(response.text)

def sljsign7206(sign_7206):
    time_369 = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.localtime())
    headers = {
        'Host': 'api.369cx.cn',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Xiaomi/Redmi 4) Cx369Android/7200 NetType/4G BusQrCodeSdkVersion/4 DarkMode/0 CityId/2500',
        'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6IiIsInJvbGUiOiJWaXNpdG9yLFVzZXIiLCJuYW1laWQiOiIxMDg3Nzk4IiwianRpIjoiOWNmYWYxYTctMmI3My00NTZhLWJjNjUtYmVjYzA2NDJkYmQxIiwibmJmIjoxNjQ0MTU5OTc2LCJleHAiOjE2NDY3NTE5NzYsImlhdCI6MTY0NDE1OTk3NiwiaXNzIjoid2ViLjM2OWN4LmNuIiwiYXVkIjoiYXBpLndlYi4zNjljeC5jbiJ9.Jtc-hDW6EugwCGsP3ATkZWJ_G-wVEL9OlNT4xEG94n0oQ5z42ybrjr7AKzfCHJuxUlcxB2aCKNm6aHdyfsxKVGmPzvsl5Y-avqQoqxKX6_yxgTOV52HEBVjHFCctmvILE6m1FasHg-VYVSwA903IovjvhSVFbfM7yNBOlU381TJYT4oXNmjCNotyN6fI4g1xrqQVc9O0d1fAKcK-HbI3k8i1GQdKYqDAiZCdW-9tTaA3AgU1OcHiNa1Fi4xAkjo17_ht8DCdq0z7KbiDXtwZlNwP1yrp_2BqEj-Lq_ekYZp2hW_rMN_XBEIvH1WNFVTTYs3k8yWjrGR6lsXX5oWI5A',
        'sign': sign_7206,
        'cityid': '2500',
        'date': time_369,
        'accept-encoding': 'gzip',
    }
    surl = b'aHR0cHM6Ly9hcGkuMzY5Y3guY24vdjIvSW50ZWdyYWwvRGF5bHlTaWdu'
    url = base64.b64decode( surl ).decode()
    response = requests.get(url, headers=headers)
    print(response.text)
    
def sljsign0883(sign):
    time_369 = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.localtime())

    headers = {
        'Host': 'api.369cx.cn',
        'cityid': '2500',
        'accept': '*/*',
        'geo': 'F%DHIY0',
        'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6IiIsInJvbGUiOiJWaXNpdG9yLFVzZXIiLCJuYW1laWQiOiI4NzEyODkiLCJqdGkiOiIyZWU2OTVkNS1lNzQ4LTRkZjYtOWI5NC1mNmM3ZmVlYjRiNTIiLCJuYmYiOjE2NDE4MTY0ODcsImV4cCI6MTY0NDQwODQ4NywiaWF0IjoxNjQxODE2NDg3LCJpc3MiOiJ3ZWIuMzY5Y3guY24iLCJhdWQiOiJhcGkud2ViLjM2OWN4LmNuIn0.bSZTulyfkI8HjBLovYLhqjleX96Nenv-s3yC-kx2xALqnYBNhHjkaB78T_lAgx2RspvpNHrigQ55eJCVYc3xrS8BgJ13VrUvLo3Cg54ganGN_kGZd0mjGnomJl6hL1p81x3-Fl4mSy2Yu8ioPvQEYd4UYjc6pojVcuWLF0HTiY6PrXVJOpK0uaCh8p5EhieH6l7o_bMbOooibaft1g1u7dfP6dLl028Ne-wFx-XhUX3vAWGDm74f9Aat8zqRdr4oo3JXQwVsMpQ_Exw_40x87UqsyxWtfcSGGalFLJDyScaE1SL0-SZ2kKNplXA6xTLaqV4g4X_3pyd6oPC7xqZvXQ',
        'sign': sign,
        'date': time_369,
        'accept-language': 'zh-Hans-CN;q=1, en-CN;q=0.9',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X; iPhone_SE) Cx369iOS/7200 NetType/WIFI DarkMode/1 BlindMode/0',
    }

    surl = b'aHR0cHM6Ly9hcGkuMzY5Y3guY24vdjIvSW50ZWdyYWwvRGF5bHlTaWdu'
    url = base64.b64decode( surl ).decode()
    response = requests.get(url, headers=headers)
    print(response.text)

def sljsign2695(sign):
    time_369 = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.localtime())

    headers = {
        'Host': 'api.369cx.cn',
        'cityid': '2500',
        'accept': '*/*',
        'geo': 'F$\'(CF2',
        'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6IiIsInJvbGUiOiJWaXNpdG9yLFVzZXIiLCJuYW1laWQiOiIxMDg3NTI1IiwianRpIjoiMzY4YTQ1MDctMTBkOC00ZDQxLWIzNjQtZGYzNzYxODdjMTZlIiwibmJmIjoxNjQ0MjQ1NDQ4LCJleHAiOjE2NDY4Mzc0NDgsImlhdCI6MTY0NDI0NTQ0OCwiaXNzIjoid2ViLjM2OWN4LmNuIiwiYXVkIjoiYXBpLndlYi4zNjljeC5jbiJ9.TxfhfOyaVdebegwNFbAs17KCn8SvxrRyWTfStO83_PMTs7pwLplLHSbtKibHqW1KxPPl1vtCSQm3z6RSYi2mukS7p04zBk6CA-fJIhLMeveriCCZg8wVMeZcEzI9E1v7twxE_QvbPQ6_3PrCnip1Lumvod7btopWOo1dQEwatZ6kv42BoYyfirQQoFsrGcUVNfOjV0bDYn5pWswa_b0FyjxtV9GNlfXTKrQrVpcQKZD63OYJeAef0l1DRmEmIAOdfPhtQdJT_SaQW02r2S8Gy2LANdPibRgekD-zudjl4rpd2eiydIFOBRADFNf-UtBU6hGR3TE380RMdK27Y0CrwA',
        'sign': sign,
        'date': time_369,
        'accept-language': 'zh-Hans-CN;q=1, en-CN;q=0.9',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X; iPhone_SE) Cx369iOS/7200 NetType/WIFI DarkMode/1 BlindMode/0',
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

def smzdm():
    cookies = {
        '__ckguid': 'lSl2Jebu7LEObg97iC5hqP',
        'device_id': '10208344591637932442029475da194266cc01d7584f6a9f623b668b7f',
        '__jsluid_s': '16d9f08ecc128e0903f99241228b6b5d',
        'homepage_sug': 'b',
        'r_sort_type': 'score',
        'Hm_lvt_9b7ac3d38f30fe89ff0b8a0546904e58': '1641903770',
        'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2217d5c618b1b1f6-0465420477f41a-734d264e-1049088-17d5c618b1c283%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217d5c618b1b1f6-0465420477f41a-734d264e-1049088-17d5c618b1c283%22%7D',
        'sess': 'AT-nLvFYHStsYzunQoIfdPYND4dO7aTer%2B8FD2IZqu5yNWfBgMI3rgRSg8L8NT3x7bP1%2BNjt%2FmToaC3GEdWLCKQB63UGvvMTtxup8PgMhqdLZ6DV55VHDfvvw0G',
        'user': 'user%3A5336577653%7C5336577653',
        'smzdm_id': '5336577653',
        'Hm_lpvt_9b7ac3d38f30fe89ff0b8a0546904e58': '1641903889',
        '_zdmA.uid': 'ZDMA.QEvnM2Dgz.1641903889.2419200',
    }

    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '"Chromium";v="21", " Not;A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4621.0 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Dest': 'script',
        'Referer': 'https://www.smzdm.com/',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    params = (
        ('callback', 'jQuery112406748769016846299_1641903888553'),
        ('_', '1641903888556'),
    )
    surl = b'aHR0cHM6Ly96aGl5b3Uuc216ZG0uY29tL3VzZXIvY2hlY2tpbi9qc29ucF9jaGVja2lu'
    url = base64.b64decode( surl ).decode()
    response = requests.get(url, headers=headers, params=params, cookies=cookies)
    print(response.text)
    
def abcBean():
    cookies = {
        'sclfyxlife_abchina_mobile_id': 'x3polt0xub11my04jvhkdwzx',
        'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2217ddd90924117d-07f0c267cdfe744-3f5f5b26-181760-17ddd909243654%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217ddd90924117d-07f0c267cdfe744-3f5f5b26-181760-17ddd909243654%22%7D',
        'BIGipServerpool_sclf_yx': '!y0yOPYKMDjhXnO0EZa3sYa6vmZstMfuVWk6V8eGlgGQWF9iGPH/OKBWy7sQSysNBxHpp8yy0VjXPoA==',
        'BIGipServerpool_sclf_yx_web': '!tV5V7pKdCHc2fzwEZa3sYa6vmZstMexMBt0u6QqH10j1lU18YX99VezCTbNUxee62lEFI1QCIxTwUQ==',
        'route': '62e13e4e62ac140ce3bfd1146a661b16',
        'BIGipServerpool_sclf_yx_engine_web': '!QKLACdUZcEyL75MEZa3sYa6vmZstMb7xK6AfQd/cXJ8eSAjqBzykR/lY5Mj54vVMtvN7L/Q8DoJbEA==',
        'JSESSIONID': '0000fhfJuglRvWDNKCNZ4Jxhigp:1f1f7pbqc',
    }
    
    headers = {
        'Host': 'enjoy.abchina.com',
        'Origin': 'https://enjoy.abchina.com',
        'Content-Type': 'application/json',
        'Accept-Language': 'en-us',
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/18F72 NebulaSDK/1.8.100112 Nebula Bankabc/Portal BankabciPhone/7.0.0 rv:7.0.3 iOS/14.6WK PSDType(1) mPaaSClient/7.0.3',
        'Referer': 'https://enjoy.abchina.com/yx/beanhome2021?from=ebank&clearStorage=true',
    }
    
    data = '{}'
    surl = b'aHR0cHM6Ly9lbmpveS5hYmNoaW5hLmNvbS95eC13ZWIvYmVhbkRldGFpbC9zaWduSW4='
    url = base64.b64decode( surl ).decode()
    response = requests.post(url, headers=headers, cookies=cookies, data=data)
    print(response.text)
    
if __name__ == '__main__':
    # 日志配置
    logger = log_setting()

#     if len(sys.argv) != 13:
#         raise Exception("传入参数不正确！")

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
    
    sign_7206 = sys.argv[13]
    sign_8958 = sys.argv[14]
    sign_2695 = sys.argv[15]
    sign_0883 = sys.argv[16]

    # 话费够
    # hfgoSign(atpAuthToken, mobile, userId, userSig)
    #     永辉生活 已注销账号
    #     yhsign(memberid, access_token, deviceid, sign)
    # 公交
    
    SHA_TZ = timezone(
        timedelta(hours=8),
        name='Asia/Shanghai',
    )
    # 协调世界时
    utc_now = datetime.utcnow().replace(tzinfo=timezone.utc)
    beijing_now = utc_now.astimezone(SHA_TZ)
    print(beijing_now, beijing_now.tzname())
    
#     smzdm()
#     sljsign0883(sign_0883)
#     sljsign7207(sign_7207)
#     sljsign8291(sign_8291)
    
#     sljsign7206(sign_7206)
#     sljsign8958(sign_8958)
#     sljsign2695(sign_2695)


 
