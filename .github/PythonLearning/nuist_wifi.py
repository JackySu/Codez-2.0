'''
原脚本由墨滢提供，我只是个打包的
'''
from pywifi import *
import requests
import base64
import os
import sys
import time
import json


MAX_RETRY = 10
WAIT_TIME = 2


def post_connect(username, domain, password):
    password = base64.b64encode(password.encode('utf-8')).decode('utf-8')
    data = {
        'username': username,
        'domain': domain,
        'password': password,
        'enablemacauth': 0
    }
    headers = {
        'User-Agent':
        r'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Origin': r'http://a.nuist.edu.cn',
        'Referer': r'http://a.nuist.edu.cn/index.php'
    }
    url = r'http://a.nuist.edu.cn/index.php/index/login'
    try:
        r = requests.post(url, data=data, headers=headers).json()
    except:
        return False
    if r['info'] in ('认证成功', '用户已登录'):
        if r['info'] == '认证成功':
            return r['logout_location']
        return True
    else:
        print(r)
        return False


def connect_nuist(username, domain='CMCC', password='123321'):
    '''
domain:
    中国移动 CMCC
    中国电信 ChinaNet
    中国联通 Unicom
    南京信息工程大学 NUIST
'''
    wifi = PyWiFi()
    ifaces = wifi.interfaces()[0]
    print('网卡读取成功')
    ifaces.disconnect()
    print('初始化成功')
    ifaces.scan()
    print('正在扫描wifi')
    temp = ifaces.scan_results()
    found = False
    for each in temp:
        print(
            '[INFO ]%s%s\t%s loaded' %
            (each.bssid, each.signal, each.ssid.encode('ISO-8859-1').decode()))
        if each.ssid == 'i-NUIST':
            profile = each
            found = True
    if not found:
        print('[ERROR]没有找到校园网！请检查网卡设置 或检查是否能扫描到i-NUIST')
        return False
    print('扫描到i-NUIST\n正在连接')
    ifaces.connect(profile)
    time.sleep(2)
    print('连接成功 正在登陆')
    retryi = 0
    while True:
        ttst = post_connect(username, domain, password)
        if ttst is not False:
            print('登陆成功!')
            if isinstance(ttst, str):
                print('已于 %s 登陆校园网' % ttst)
            return True
        else:
            if retryi > MAX_RETRY:
                print('[ERROR]登陆失败！')
                return False
            retryi += 1
            print('[ERROR]登陆失败！正在重试(%s)' % (retryi))
            time.sleep(WAIT_TIME)


if __name__ == '__main__':
    login = []
    with open('config.ini', 'r') as f:
        for line in f.readlines():
            line = line.strip()
            if line[0] != '#':
                login.append(line)

    try:
        connect_nuist(login[0], login[1], login[2])
        '''
登陆方式：
    中国移动 CMCC
    中国电信 ChinaNet
    中国联通 Unicom
    南京信息工程大学 NUIST
'''
        os.system('pause')
    except:
        print('出现了错误:\n')
        import traceback
        print(traceback.format_exc())
        os.system('pause')
