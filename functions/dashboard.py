from discord.ext import commands
from discord.ui import View

from utils.commons import create_or_update_user
from utils.constants import FRONTEND_ENDPOINT
from component.linkButton import LinkButton


class Dashboard(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(aliases=['dashboard'])
    async def view_info(self, ctx) -> None:
        from_id = ctx.author.id
        from_name = ctx.author.name
        from_discriminator = ctx.author.discriminator
        from_avatar = ctx.author.avatar
        create_or_update_user(from_id, from_name, from_discriminator, from_avatar)

        url = f"{FRONTEND_ENDPOINT}/dashboard?fromId={from_id}"
        link_button = LinkButton(label="Go to Dashboard!", url=url)

        view = View()
        view.add_item(link_button)

        await ctx.send("Click Button for going Genie dashboard :genie:", view=view, ephemeral=True)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        Dashboard(bot)
    )