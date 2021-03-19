import requests
from bs4 import BeautifulSoup


def get_nytimes_article():

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
    response = requests.get(
        "https://www.nytimes.com/section/technology", headers=headers)

    print("Response: ", response)

    soup = BeautifulSoup(response.content, 'lxml')

    article_info = soup.select("div a", attrs={"class": "css-1l4spti"})
    article_url = "https://www.nytimes.com" + article_info[44].get('href')
    article_title = article_info[44].find('h2').get_text()
    article_description = article_info[44].find('p').get_text()

    return [article_url, article_title, article_description]


# get_nytimes_article()
