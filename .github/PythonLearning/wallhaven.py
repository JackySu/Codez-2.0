import requests
import re
import os


def getImg(n):
    url = 'https://alpha.wallhaven.cc/wallpaper/'  # 图片对应的网站
    pattern = r'//wallpaper.+?(jpg|png)'  # 匹配图片的正则
    path = 'C:/Users/oi/Pictures'  # 图片存储路径
    for i in range(n):
        r = requests.get(url + str(i + 1))
        r.encoding = r.apparent_encoding
        mattch = re.search(pattern, r.text)
        if mattch:
            img = requests.get("https:" + mattch.group(0))
            if not os.path.exists(path):  # 保存图片的路径不存在则创建
                os.mkdir(path)
            if img.url.endswith('.jpg'):  # 不同格式的图片
                with open('C:/Users/oi/Pictures/t' + str(i + 1) + '.jpg',
                          'wb') as f:
                    f.write(img.content)  # 将图片保存到本地
                    f.close()
            elif img.url.endswith('.png'):
                with open('C:/Users/oi/Pictures/t' + str(i + 1) + '.png',
                          'wb') as f:
                    f.write(img.content)
                    f.close()
            else:
                print('爬取失败，图片后缀为：' + img.url[-4:])
            print('第' + str(i + 1) + '次爬取\t成功！')
        else:
            print("第{}次爬取\t失败!".format(i + 1))


def main():
    getImg(20)  #这里仅爬取20张图片


main()
# ————————————————
# 版权声明：本文为CSDN博主「除离」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/qq_38338669/article/details/81366928