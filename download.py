import requests
import re
from lxml import etree
import time
import cloudscraper


uri = r'https://m.ddtxt8.cc'
book = r'/book/73206/'
path = r'~/Documents/Code/Self/downloadtxt/zz/'

scraper = cloudscraper.create_scraper()

def get_text(local_url):
    # r = requests.get(local_url)
    r = scraper.get(local_url)
    r.encoding = 'utf-8'
    selector = etree.HTML(r.text)
    title = selector.xpath('/html/head/title/text()')
    real_title = ''.join((ch if ch in '0123456789.-e' else '') for ch in title[0])
    print(real_title)

    text = selector.xpath('//*[@id="chaptercontent"]/text()')
    # TODO: replace two space to new line
    with open(path+real_title+'.txt', 'a+', encoding='utf-8') as f:
        for i in text:
            s1 = re.sub("请收藏：https://m.ddtxt8.cc", "", i)
            f.write(s1)
    n_url = selector.xpath('//a/@href')
    print(n_url)
    time.sleep(1)
    return n_url[4]


if __name__ == '__main__':
    for page_num in range(1, 3257):
        url = uri + book + str(page_num) + '.html'
        print(url)
        next_page = get_text(url)
        print(next_page)
        next_number = re.sub('_.?.html$', '', next_page.split('/')[3])
        print(next_number)
        print('page_num {}'.format(page_num))
        while next_number == str(page_num):
            print('should get page {}'.format(uri+next_page))
            next_page = get_text(uri + next_page)
            print(next_page)
            next_number = re.sub('_.?.html$', '', next_page.split('/')[3])
            print(next_number)
            print('page_num {}'.format(page_num))
