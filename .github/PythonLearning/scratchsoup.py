import json
import requests
from bs4 import BeautifulSoup
import lxml
import xlwt


def main(page):
    url = 'https://movie.douban.com/top250?start=' + str(
        page * 25) + '&filter='
    html = request_douban(url)
    soup = BeautifulSoup(html, 'lxml')
    parse_result(soup)
    save_to_excel(soup)


def request_douban(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


def parse_result(soup):

    Getlist = soup.find(class_='grid_view').find_all('li')

    for item in Getlist:
        item_name = item.find(class_='title').string
        item_img = item.find('a').find('img').get('src')
        item_index = item.find(class_='').string
        item_score = item.find('p').text
        item_intr = item.find(class_='inq').string

        print('爬取电影：' + item_index + ' | ' + item_name + ' | ' + item_score +
              ' | ' + item_intr)


def save_to_excel(soup):

    book = xlwt.Workbook(encoding='utf-8', style_compression=0)

    sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)
    sheet.write(0, 0, '名称')
    sheet.write(0, 1, '图片')
    sheet.write(0, 2, '排名')
    sheet.write(0, 3, '评分')
    sheet.write(0, 4, '作者')
    sheet.write(0, 5, '简介')
    sheet.write(n, 0, item_name)
    sheet.write(n, 1, item_img)
    sheet.write(n, 2, item_index)
    sheet.write(n, 3, item_score)
    sheet.write(n, 4, item_author)
    sheet.write(n, 5, item_intr)


if __name__ == '__main__':
    for i in range(10):
        main(i)
