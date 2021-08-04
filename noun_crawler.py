from bs4 import BeautifulSoup
import requests

DOMAIN = "https://ko.wiktionary.org"
URL = DOMAIN + "/wiki/%EB%B6%84%EB%A5%98:%ED%95%9C%EA%B5%AD%EC%96%B4_%EB%AA%85%EC%82%AC"
html = requests.get(URL).text
soup = BeautifulSoup(html, 'html.parser')


category = soup.find_all("a", class_="external text")

# print(speic[0])
# print(speic[5])

word_section = soup.find("div", id="mw-pages")
word_group = word_section.find("div", class_="mw-category-group")
wordList = word_group.find_all("a")

# print(wordList[0])
# print(wordList[0].get('href'))


DETAIL_URL = DOMAIN + wordList[79].get('href')
print(DETAIL_URL)

detailHtml = requests.get(DETAIL_URL).text
detailSoup = BeautifulSoup(detailHtml, 'html.parser')

detail_section = detailSoup.find("div", class_="mw-parser-output")

detail_group = detail_section.find_all("ul")
print(detail_group)


# if(detail_group.length > 0):
#     print(detail_group[0])
# else:
#     print('No Details')


