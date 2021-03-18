from praw.models import InlineImage


def build_template(articles, meme):

    meme_path = meme[0]
    meme_caption = meme[1]

    image = InlineImage(meme_path, meme_caption)
    media = {"image1": image}

    title = "📍 Markdown template"
    selftext = """Hello 👋 Today's botly news articles are:
* [First news article](https://markdownlivepreview.com/) Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae scelerisque ipsum. Duis imperdiet arcu nulla, quis rhoncus risus porttitor nec. Etiam sit amet posuere diam.  
* [Second news article](https://markdownlivepreview.com/) Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae scelerisque ipsum. Duis imperdiet arcu nulla, quis rhoncus risus porttitor nec. Etiam sit amet posuere diam.  
* [Third news article](https://markdownlivepreview.com/) Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae scelerisque ipsum. Duis imperdiet arcu nulla, quis rhoncus risus porttitor nec. Etiam sit amet posuere diam.  
{image1}
    """
    return [title, selftext, media]
