import requests
import json


word = input("Enter the text you want to translate: ")
url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
From_data = {'i': word,
             'from': 'zh-CHS',
             'to': 'en',
             'smartresult': 'dict',
             'client': 'fanyideskweb',
             'salt': '15742300938227',
             'sign': 'db547a660d8aab58571bb691f2b47c08',
             'ts': '1574230093822',
             'bv': 'd0e49aa81d879baaa28d12b34fc4a5d5',
             'doctype': 'json',
             'version': '2.1',
             'keyfrom': 'fanyi.web',
             'action': 'FY_BY_REALTIME'
            }

response = requests.post(url, data=From_data)
content = json.loads(response.content)
print(content['translateResult'][0][0]['tgt'])
