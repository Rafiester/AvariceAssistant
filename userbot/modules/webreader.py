# import from pyrobud custom modules
# edited by alanndz

import random
import re

from newspaper import Article, ArticleException
from telegraph import Telegraph
from googletrans import Translator, LANGUAGES

from userbot import CMD_HELP, bot
from userbot.events import register

WR_LANG = "id"
regex: str = r'(https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.' \
		r'[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&\/\/=]*))'

tgr = Telegraph()
tl = Translator()

@register(outgoing=True, pattern=r"^\.wr(?: |$)(.*)")
async def webread_tl(web):
    link = web.pattern_match.group(1)
    if not link:
        return await web.edit("`No link given`")

    if link.split()[0] == "lang":
        global WR_LANG
        lang = link.split()
        if len(lang) == 1:
            return await web.edit(
                f"`Available language codes for WR`:\n\n`{LANGUAGES}`"
            )

        lang = lang[1]

        if lang in LANGUAGES:
            WR_LANG = lang
            return await web.edit(
                "Success change default lang to `%s`"%(LANGUAGES[lang])
            )
        else:
            return await web.edit(
                f"`Invalid Language code !!`\n`Available language codes for WR`:\n\n`{LANGUAGES}`"
            )

    url: str = re.search(regex, link).group(1)

    article: Article = Article(url)

    try:
        await web.edit("Getting text ...")
        article.download()
        article.parse()
        tex = f"{article.text}"
    except ArticleException:
        return await web.edit("Failed to scrape the article!")

    try:
        await web.edit("Translating Text to `{}` ...".format(WR_LANG))
        tex = tl.translate(tex, dest=WR_LANG, src="auto")
        tex = tex.text
    except ValueError as err:
        return await web.edit("Error: `{}`".format(str(err)))

    await web.edit("Uploading to telegraph ...")
    tgr.create_account(short_name='13378')
    response = tgr.create_page(
        f"{article.title}",
        html_content="<p>{}</p>".format(tex.replace("\n", "<br>"))
    )

    await web.edit(
        f"**Title:**\n`{article.title}`\n**Source:**\n`{url}`\n\nTranslated: [Click Here](https://telegra.ph/{response['path']})"
    )


CMD_HELP.update(
    {
        "webreader": ">`.wr`"
        "\nUsage: .wr <link> to scrape web, translate, then upload to telegraph."
        "\n`.wr lang` <lang target> to change default language."
    }
)
