# coding = utf-8

import requests
import re
import time
from fake_useragent import UserAgent

# 使用正则表达式爬取数据
def paShuDan(pageNum):
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    print(headers)
          #https://www.yousuu.com/booklists/?type=man&screen=comprehensive&page=2
    url = 'https://www.yousuu.com/booklists/?type=man&screen=comprehensive&page=2' + str(pageNum)
    respon = requests.get(url, headers=headers, timeout=10)
    print(respon.status_code)
    content = respon.text
    file = open("./yousuuHTML.txt",mode='a',encoding="utf8")
    file.write(content)
    file.close()
    pattern = re.compile('booklist-card-content.*?href="/(.*?)".*?>(.*?)<.*?userinfo-avatar.*?>(.*?)<', re.S)
    results = re.findall(pattern, content)

    for results in results:
        print("1")
        url, listname, username = results
        print(url, username, username)

def main():
    maxPage = 1
    i = 1
    while i <= maxPage :
        paShuDan(i)
        i = i + 1
        time.sleep(3)

if __name__ == '__main__':
    main()

