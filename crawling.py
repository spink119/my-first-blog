import urllib.request
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/news/news_list.nhn?mode=LSS2D&section_id=101&section_id2=258'

html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')

# title = soup.find_all(class_='articleSubject')

# for i in title:
#     print(i.find('a',{'title':'title'}))
        #  print(i.attrs['href'])
print(soup.prettify())
