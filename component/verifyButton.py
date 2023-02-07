from discord import ButtonStyle
from discord.ui import Button, View

from component.linkButton import LinkButton
from utils.constants import FRONTEND_ENDPOINT


class VerifyButton(Button):
    def __init__(self, label, user_id):
        super().__init__(label=label, style=ButtonStyle.primary)
        self.user_id = user_id

    async def callback(self, interaction):
        verify_url = f"{FRONTEND_ENDPOINT}/mypage?fromId={self.user_id}&autoVerify=true"
        link_button = LinkButton(label="Go to verifying!", url=verify_url)
        view = View()
        view.add_item(link_button)

        await interaction.response.send_message(view=view, ephemeral=True)