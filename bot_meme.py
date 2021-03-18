import re
import praw
import requests
from bs4 import BeautifulSoup
from praw.models import InlineImage

meme_dict = {}


def main():
    reddit = praw.Reddit(
        user_agent="LMGTFY (by u/Skeeter-the-bot)",
        client_id="BA_gWuIWrXfv6A",
        client_secret="wz_t6cgZbKXbAEjr0ygXhbq9N-8PbQ",
        username="Skeeter-the-bot",
        password="SkeeterBot",
    )

    subreddit = reddit.subreddit("ProgrammerHumor")

    src = get_best_meme(subreddit)


def get_best_meme(subreddit):

    add_memes_to_dict(subreddit)

    post_title, post_link = best_meme_in_dict(meme_dict)

    return get_meme_src(subreddit, post_title, post_link)


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


def best_meme_in_dict(meme_dict):
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


if __name__ == "__main__":
    main()
