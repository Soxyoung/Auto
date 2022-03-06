import requests
    #因为并不是每个IP都是能用，所以要进行异常处理
try:
    proxy = {
        'http':'47.92.234.75:80'
    }
    url1 = 'https://www.baidu.com/'
    #遍历时，利用访问百度，设定timeout=1,即在1秒内，未送到响应就断开连接
    res = requests.get(url=url1,proxies=proxy,timeout=1)
    #打印检测信息，elapsed.total_seconds()获取响应的时间
    print('47.92.234.75:80' +'--',res.elapsed.total_seconds())
except BaseException as e:
    print(e)
