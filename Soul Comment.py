import requests
from bs4 import BeautifulSoup

url = []
for start_value in range(0, 220, 20):
    example = "https://movie.douban.com/subject/{}/comments?start={}&limit=20&status=P&sort=new_score".format("24733428", start_value)
    url.append(example)
for i in range(len(url)):
    print(url[i])
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Chrome/ 90.0.4430.93 Safari/605.1.15'}
r = []
soup = []
short_comment = []
for i in range(len(url)):
    r.append(requests.get(url[i], headers=headers))
    soup.append(BeautifulSoup(r[i].text, "html.parser"))
    short_comment.extend(soup[i].find_all('span', class_='short'))
for i in range(len(short_comment)):
    short_comment[i] = short_comment[i].string
    print(short_comment[i])
filename = 'Soul Comment.txt'
open(filename, 'w+', encoding='utf-8')
for i in range(len(short_comment)):
    with open(filename, 'a+', encoding='utf-8') as file_object:
        file_object.write(str(i + 1) + '. ' + short_comment[i] + '\n\n')