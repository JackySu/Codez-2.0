import pywifi
import os
import traceback
from pywifi import *
import requests
import base64
import sys
import time

MAX_RETRY = 5
WAIT_TIME = 2

def post_connect(username, domain, password):
    password = base64.b16encode(password.encode('utf-8')).decode('utf-8')
    data = {'username': username,
            'domain': domain,
            'password': password,
            'enablemacauth': 0}
    headers = {'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
               'Origin': r'http://a.nuist.edu.cn',
               'Referer':r'http://a.nuist.edu.cn/index.php'}
    url = r'http://a.nuist.edu.cn/index.php/index/login'
    try:
        r = requests.post(url, data=data, headers=headers).json()
    except:
        return False
    if r['info'] in ('认证成功','用户已登录'):
        if r['info'] == '认证成功':
            return r['logout_location']
        return True
    else:
        print(r)
        return False


if __name__ == '__main__':
    try:
        connect_nuist('','','')
        '''
移动CMCC
电信ChinaNet
联通Unicom
南信大NUIST
'''
        os.system('pause')
    except:
        print('错误:\n')
        print(traceback.format_exc())
        os.system('pause')
