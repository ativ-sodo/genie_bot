import requests

from utils.constants import BACKEND_ENDPOINT


def create_or_update_user(id, name, discriminator, avatar):
    open_bracket = '{'
    close_bracket = '}'
    body = f"""
    mutation {open_bracket}
        createOrUpdateUserInfo(
            discordId: "{id}"
            name: "{name}"
            discriminator: {str(discriminator)}
            avatar: "{avatar}"
        ) {open_bracket}
            success
        {close_bracket}
    {close_bracket}
    """

    print(body)
    response = requests.post(url=BACKEND_ENDPOINT, json={"query": body})
    print(response.content)


def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False