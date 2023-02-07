from discord.ext import commands
from discord.ui import View

from utils.commons import create_or_update_user, is_float
from utils.constants import COIN, FRONTEND_ENDPOINT
from component.linkButton import LinkButton


class Send(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @staticmethod
    def _is_discord_handle(handle_str):
        return handle_str[0] == '<' and handle_str[1] == '@' and handle_str[-1] == '>' and handle_str[2:-1].isdecimal()

    @commands.command()
    async def send(self, ctx, *args) -> None:
        from_id = ctx.author.id
        from_name = ctx.author.name
        from_discriminator = ctx.author.discriminator
        from_avatar = ctx.author.avatar
        create_or_update_user(from_id, from_name, from_discriminator, from_avatar)

        args = list(args)

        if len(args) == 3:
            args[0] = args[0].upper()
            args[1] = args[1].upper()

            if args[0] == 'NFT' and args[1] == 'TO' and self._is_discord_handle(args[2]):
                url = f"{FRONTEND_ENDPOINT}/sendtoken?fromId={from_id}&toId={args[2][2:-1]}"
                link_button = LinkButton(label="Go to send NFT!", url=url)

                to_user = await self.bot.fetch_user(args[2][2:-1])
                channel = await to_user.create_dm()
                await channel.send("Check your wallet. :genie:")

                view = View()
                view.add_item(link_button)

                await ctx.send("Click Button for sending NFT through Genie service :genie:", view=view, ephemeral=True)
            else:
                await ctx.send('Invalid Commands. Check commands ser :genie:', ephemeral=True)
        elif len(args) == 4:
            args[1] = args[1].upper()
            args[2] = args[2].upper()

            if is_float(args[0]) and args[1] in COIN.keys() and self._is_discord_handle(args[3]):
                url = f"{FRONTEND_ENDPOINT}/sendcoin?coin={COIN[args[1]]}&amount={str(float(args[0]))}&fromId={from_id}&toId={args[3][2:-1]}"
                link_button = LinkButton(label="Go to send coin!", url=url)

                to_user = await self.bot.fetch_user(args[3][2:-1])
                channel = await to_user.create_dm()
                await channel.send("Check your wallet. :genie:")

                view = View()
                view.add_item(link_button)

                await ctx.send("Click Button for sending coin through Genie service :genie:", view=view, ephemeral=True)
            else:
                await ctx.send('Invalid Commands. Check commands ser :genie:', ephemeral=True)
        else:
            await ctx.send('Invalid Commands. Check commands ser :genie:', ephemeral=True)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        Send(bot)
    )