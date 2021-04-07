import re
import praw
import requests
from bs4 import BeautifulSoup

meme_dict = {}


def download_best_meme(subreddit):
    """Returns the link for the most upvoted meme in the subreddit"""

    add_memes_to_dict(subreddit)

    post_title, post_link = get_best_meme_in_dict(meme_dict)

    url = get_meme_src(subreddit, post_title, post_link)

    response = requests.get(url)
    file = open("current_meme.png", "wb")
    file.write(response.content)
    file.close()

    return post_title


def add_memes_to_dict(subreddit):
    """Adds the 5 hottest posts to the meme_dict"""

    meme_count = 1
    for submission in subreddit.hot(limit=5):
        meme_dict[f'meme_{meme_count}'] = [
            submission.score,
            submission.title.encode("utf-8"),
            "https://www.reddit.com" + submission.permalink
        ]

        meme_count += 1


def get_best_meme_in_dict(meme_dict):
    """Returns the title, link of the most upvoted post from the meme_dict"""
    key_most_upvoted = max(meme_dict, key=meme_dict.get)
    post_title = str(meme_dict[key_most_upvoted][1])[2:-1]
    post_link = meme_dict[key_most_upvoted][2]

    print("Title:", post_title, "\nLink:", post_link)

    return post_title, post_link


def get_meme_src(subreddit, post_title, post_link):
    """Returns the image src of the post_link"""

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
    response = requests.get(post_link, headers=headers)

    print("Response: ", response)

    soup = BeautifulSoup(response.content, 'lxml')

    img_info = str(
        soup.find("img", attrs={"alt": f"r/{subreddit} - {post_title}"}))

    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    src = re.search(regex, img_info)

    print("Img src: ", src.group())

    return src.group()
