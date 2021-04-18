from bs4 import BeautifulSoup
import requests


def get_text(url):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, 'lxml')
    return soup.get_text()


def summarize(text):
    API_KEY = "8642137C4E"
    API_ENDPOINT = "https://api.smmry.com"

    data = {
        "sm_api_input": text
    }
    params = {
        "SM_API_KEY": API_KEY,
        "SM_LENGTH": 2
    }
    header_params = {"Expect": "100-continue"}
    r = requests.post(url=API_ENDPOINT, params=params,
                      data=data, headers=header_params)

    return r.json()


# url = "https://www.nytimes.com/2021/04/16/science/spacex-moon-nasa.html"
# text = get_text(url)

# sum_text = summarize(text)['sm_api_content']
# print(sum_text)
