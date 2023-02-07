from discord import ButtonStyle
from discord.ui import Button


class LinkButton(Button):
    def __init__(self, label, url):
        super().__init__(label=label, url=url, style=ButtonStyle.link)
        self.url = url