from discord.ext import commands
from discord.ui import View

from utils.commons import create_or_update_user
from component.verifyButton import VerifyButton


class Verify(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(aliases=['verify'])
    async def verify_wallet(self, ctx) -> None:
        from_id = ctx.author.id
        from_name = ctx.author.name
        from_discriminator = ctx.author.discriminator
        from_avatar = ctx.author.avatar
        create_or_update_user(from_id, from_name, from_discriminator, from_avatar)

        verify_button = VerifyButton("Verify", from_id)

        view = View()
        view.add_item(verify_button)

        await ctx.send("Click Verify for using Genie service :genie:", view=view, ephemeral=True)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        Verify(bot)
    )