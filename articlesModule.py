import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}


def get_nytimes_article():

    response = requests.get(
        "https://www.nytimes.com/section/technology", headers=headers)

    print("Response from NYT: ", response)

    soup = BeautifulSoup(response.content, 'lxml')

    article_info = soup.select("div a", attrs={"class": "css-1l4spti"})
    article_url = "https://www.nytimes.com" + article_info[44].get('href')
    article_title = article_info[44].find('h2').get_text()
    article_description = article_info[44].find('p').get_text()

    return [article_title, article_url, article_description]


def get_wired_article():

    response = requests.get(
        "https://www.wired.com/category/science/", headers=headers)

    print("Response from Wired: ", response)

    soup = BeautifulSoup(response.content, 'lxml')

    article_info = soup.find_all(
        "a", attrs={"class": "post-listing-list-item__link"})

    article_url = "https://www.wired.com" + article_info[8].get('href')
    article_title = article_info[8].find('h5').get_text()
    article_description = ""

    return [article_title, article_url, article_description]


def get_mit_article():

    response = requests.get(
        "https://www.technologyreview.com/", headers=headers)

    print("Response from MIT: ", response)

    soup = BeautifulSoup(response.content, 'lxml')

    article_info = soup.find(
        "a", attrs={"class": "popular__itemTitle--3oYx0"})

    article_url = article_info.get('href')
    article_title = article_info.get_text()
    article_description = ""

    return [article_title, article_url, article_description]
