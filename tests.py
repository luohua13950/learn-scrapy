__author__ = 'luohua139'
import requests

def telnet():
    url = "https://www.baidu.com/"
    url = "https://hao.360.com/?wd_xp1"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
    }
    prx = {
        "https":"https://125.94.44.129:1080"
    }
    rsp = requests.get(url,headers = headers,timeout = 10)
    print(rsp.text)


if __name__ == '__main__':
    telnet()