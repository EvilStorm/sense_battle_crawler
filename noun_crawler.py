from bs4 import BeautifulSoup
import requests
import json

TARGET_DOMAIN = "https://ko.wiktionary.org"
API_URL = "http://localhost:2394/api/noun"

def startCrawling():
    URL = TARGET_DOMAIN + "/wiki/%EB%B6%84%EB%A5%98:%ED%95%9C%EA%B5%AD%EC%96%B4_%EB%AA%85%EC%82%AC"
    start(URL)


def start(url):
    
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')

    category = soup.find_all("a", class_="external text")

    loadCrawlerPage(category[0].get('href'))
    #다음으로 넘어가기 하면 ㄴ, ㄷ, ㄹ 으로 계속 넘어간다. 
    # for temp in category:
    #     print(temp)
    #     loadCrawlerPage(temp.get('href'))

def loadCrawlerPage(url): 

    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')


    word_section = soup.find("div", id="mw-pages")
    word_group = word_section.find("div", class_="mw-category-group")
    wordList = word_group.find_all("a")

    for word in wordList: 
        addWord(word.text, word.get('href'))

    next_page_section = soup.find("div", id="mw-pages")
    next_page_group = next_page_section.find_all("a")

    for temp in next_page_group: 
        if(temp.text == '다음 페이지'):
            loadCrawlerPage(TARGET_DOMAIN+temp.get('href'))
            break



def addWord(word, url):
    params = {
        'word': word,
        'source_url': TARGET_DOMAIN+url
    }

    result = requests.post(API_URL, params)

    if(result.status_code == 200):
        print("Add Complete: " + word)
    else:
        print("Add Fail: " + word)
    


startCrawling()
