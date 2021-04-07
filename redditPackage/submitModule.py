from praw.models import InlineImage


def build_template(articles, meme):

    image = InlineImage(path=meme[0], caption=meme[1])
    media = {"image1": image}

    title = "📍 Today's articles are here"

    article1 = f"\n * [{articles[0][0]}]({articles[0][1]}) {articles[0][2]}"
    article2 = f"\n * [{articles[1][0]}]({articles[1][1]}) {articles[1][2]}"
    article3 = f"\n * [{articles[2][0]}]({articles[2][1]}) {articles[2][2]}"

    selftext = "Hello 👋 today's botly news articles:" + \
        article1 + article2 + article3 + "{image1}"

    return [title, selftext, media]
