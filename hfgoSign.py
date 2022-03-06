import requests
    #因为并不是每个IP都是能用，所以要进行异常处理
try:
    proxy = {
        'http':'122.9.101.6:8888',
        'https':'122.9.101.6:8888'
    }


    response=requests.get("http://httpbin.org/ip",proxies=proxy)
    # response=requests.get("http://httpbin.org/ip")

    print(response.text)

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

    response = requests.get('https://atp.bol.wo.cn/atpapi/act/record/residueCount', headers=headers, params=params, cookies=cookies, proxies=proxy)
    rsp = response.text
    print(rsp)

except BaseException as e:
    print(e)
