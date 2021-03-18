import praw
from memeModule import get_best_meme
from submitModule import build_template


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

    articles = []
    meme = ["memes/meme_0.jpg", "caption"]

    template = build_template(articles, meme)

    title = template[0]
    selftext = template[1]
    media = template[2]

    reddit.subreddit("YourDailyTechNews9932").submit(
        title, selftext=selftext, inline_media=media)


if __name__ == "__main__":
    main()
