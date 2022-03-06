import requests
import base64
import calendar
import datetime
import time
import json


proxies={

'http':'47.92.234.75:80',

}

def everydaySign():
    cookies = {
        'atpAuthToken': 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODYxNTY1MDg4MyIsInBob25lIjoiMTg2MTU2NTA4ODMiLCJjcmVhdGVkIjoxNjQwMzU3ODA0NzYxLCJleHAiOjE2NDgxMzM4MDQsInVzZXJJZCI6IlUyMDIxMDEwNTE1NTgzMTY1OTQ0MDc4ZmtzMGMifQ.s_pEvob3yla07V0Z4gBA2Om-yxme4NDQXvS65_hbtuWAP286--0Zd1ZETTDMqdXwDXny0kqbznZN4OK6FYfJPw',
        'mobile': 'uXn+SOYBEybeu+gzeeLqGw==',
        'userId': 'elrBjxw8cs9gl2PhcodlpbU/yz5AN8Hohq1KRG8tTOU=',
        'userSig': 'eJxFkNtOg0AURf*FV42cYWa4*FaRpii2IgWLISEUhjIlXAJjU2r8dymh8XWtc9vnR9o63kPStjyLExHjLpMeJZDuJ8zOLe9YnOSCdSNGlFIF4GZPrOt5U49CAUSRggH*Jc9YLXjOp0ZfAQUBAjpO0DFSqUEIaHpe9pDO9T0-jIVvVmja7nNrvdv4MiRPCB9T9xwc9FM4VLpbms6d97EvnFDD*0j*bCLZd*1i8eI6BBV*Zjrb13K1GvK*0qylt1nuviI5sDfpGoxgsT6qYmfc9mVlPKW*5iLj3RgRTZml4BW7cpUAppoOZOZJmjbftYjF0LLpTb9-poFcMQ__',
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
    response = requests.get(url, headers=headers, params=params, cookies=cookies, proxies=proxies)
    print(response.text)

def lottery():
    cookies = {
        'atpAuthToken': 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODYxNTY1MDg4MyIsInBob25lIjoiMTg2MTU2NTA4ODMiLCJjcmVhdGVkIjoxNjQxODE2OTI5NTQwLCJleHAiOjE2NDk1OTI5MjksInVzZXJJZCI6IlUyMDIxMDEwNTE1NTgzMTY1OTQ0MDc4ZmtzMGMifQ.1xJLCKNtgO3HNrCxfhj8GYvDgdDa_mScN3whOhv1LSAZSeMh2QZYbWEHT5HditoGal9mHNkWxR_Vhza-ycKoJQ',
        'mobile': 'uXn+SOYBEybeu+gzeeLqGw==',
        'userId': 'elrBjxw8cs9gl2PhcodlpbU/yz5AN8Hohq1KRG8tTOU=',
        'userSig': 'eJxFkF1rgzAUhv*LtxvrSWKsDnaxiqzFtbOsCoOCBBNd-Mw06yyj-32pWHZzLt7nPR-v*bUOr*8PTCnJU6ZT0nPr0QLrfpLFqGQvUpZr0RsZUUoxwI2eRD-IrjUAA6IIE4B-KLlotczl1BhjwAgQUDPBJcihnm3D0s2rAbLZP8jCGLdB7G-2fkW8PDkDfcFDWNd9uAvK9e6uTHhZJPtArPyoG7U*4JL*bIqwA0G2ZF1-qnhsIKqPi6g1hZ7pV8VUf1wUvFHMd09vq4-np9s*XqVT6msu29xNkL3EM9SyEVfdsZGLHA97s86yrPtudarPSkxvuvwBP-Jdvg__',
    }

    headers = {
        'Host': 'atp.bol.wo.cn',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148     unicom{version:iphone_c@9.0000}{systemVersion:dis}{yw_code:}',
        'Accept-Language': 'zh-cn',
        'Referer': 'https://atp.bol.wo.cn/atplottery/ACT202009101956022770009xRb2UQ?product=hfgo',
    }

    response = requests.get('https://atp.bol.wo.cn/atpapi/act/lottery/start/v1/actPath/ACT202009101956022770009xRb2UQ/0', headers=headers, cookies=cookies, proxies=proxies)
    print(response.text)

def qCnt():
    cookies = {
        'atpAuthToken': 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODYxNTY1MDg4MyIsInBob25lIjoiMTg2MTU2NTA4ODMiLCJjcmVhdGVkIjoxNjQxODE2OTI5NTQwLCJleHAiOjE2NDk1OTI5MjksInVzZXJJZCI6IlUyMDIxMDEwNTE1NTgzMTY1OTQ0MDc4ZmtzMGMifQ.1xJLCKNtgO3HNrCxfhj8GYvDgdDa_mScN3whOhv1LSAZSeMh2QZYbWEHT5HditoGal9mHNkWxR_Vhza-ycKoJQ',
        'mobile': 'uXn+SOYBEybeu+gzeeLqGw==',
        'userId': 'elrBjxw8cs9gl2PhcodlpbU/yz5AN8Hohq1KRG8tTOU=',
        'userSig': 'eJxFkF1rgzAUhv*LtxvrSWKsDnaxiqzFtbOsCoOCBBNd-Mw06yyj-32pWHZzLt7nPR-v*bUOr*8PTCnJU6ZT0nPr0QLrfpLFqGQvUpZr0RsZUUoxwI2eRD-IrjUAA6IIE4B-KLlotczl1BhjwAgQUDPBJcihnm3D0s2rAbLZP8jCGLdB7G-2fkW8PDkDfcFDWNd9uAvK9e6uTHhZJPtArPyoG7U*4JL*bIqwA0G2ZF1-qnhsIKqPi6g1hZ7pV8VUf1wUvFHMd09vq4-np9s*XqVT6msu29xNkL3EM9SyEVfdsZGLHA97s86yrPtudarPSkxvuvwBP-Jdvg__',
    }

    headers = {
        'Host': 'atp.bol.wo.cn',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148     unicom{version:iphone_c@9.0000}{systemVersion:dis}{yw_code:}',
        'Accept-Language': 'zh-cn',
        'Referer': 'https://atp.bol.wo.cn/atplottery/ACT202009101956022770009xRb2UQ?product=hfgo',
    }

    params = (
        ('actId', '517'),
    )

    try:
        response = requests.get('https://atp.bol.wo.cn/atpapi/act/record/residueCount', headers=headers, params=params, cookies=cookies, proxies=proxies)
        rsp = response.text
        info = json.loads(rsp)
        print(info['data'])
        return info['data']
    except:
        return 3


if __name__ == '__main__':

    everydaySign()

    time.sleep(6)

    cnt = qCnt()

    for i in range(cnt):
        lottery()
        time.sleep(1)
    # currentdate = datetime.date.today()
    #
    # year= currentdate.year
    #
    # month = currentdate.month
    #
    # day = currentdate.day
    #
    # currentday =calendar.weekday(year,month,day)
    #
    # time.sleep(66)
    #
    # if currentday == 0:
    #     for j in range(3):
    #         lottery()
