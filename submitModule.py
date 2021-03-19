from praw.models import InlineImage


def build_template(articles, meme):

    image = InlineImage(path=meme[0], caption=meme[1])
    media = {"image1": image}

    title = "📍 Markdown template"

    article1 = f"\n * [{articles[0]}]({articles[1]}) {articles[2]}"
    article2 = "\n * [Second news article](https://markdownlivepreview.com/) Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae scelerisque ipsum. Duis imperdiet arcu nulla, quis rhoncus risus porttitor nec. Etiam sit amet posuere diam."
    article3 = "\n * [Third news article](https://markdownlivepreview.com/) Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae scelerisque ipsum. Duis imperdiet arcu nulla, quis rhoncus risus porttitor nec. Etiam sit amet posuere diam."

    selftext = "Hello 👋 Today's botly news articles are:" + \
        article1 + article2 + article3 + "{image1}"

    return [title, selftext, media]
