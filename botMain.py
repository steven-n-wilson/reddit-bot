import praw
from redditPackage import articlesModule, memeModule, submitModule

# from memeModule import download_best_meme
# from submitModule import build_template
# from articlesModule import get_mit_article, get_nytimes_article, get_wired_article


def main():

    reddit = praw.Reddit(
        user_agent="LMGTFY (by u/Skeeter-the-bot)",
        client_id="BA_gWuIWrXfv6A",
        client_secret="wz_t6cgZbKXbAEjr0ygXhbq9N-8PbQ",
        username="Skeeter-the-bot",
        password="SkeeterBot",
    )

    subreddit = reddit.subreddit("ProgrammerHumor")

    caption = memeModule.download_best_meme(subreddit)

    articles = [articlesModule.get_nytimes_article(
    ), articlesModule.get_wired_article(), articlesModule.get_mit_article()]
    meme = ["current_meme.png", caption]

    template = submitModule.build_template(articles, meme)

    reddit.subreddit("YourDailyTechNews9932").submit(
        title=template[0], selftext=template[1], inline_media=template[2])


if __name__ == "__main__":
    main()
