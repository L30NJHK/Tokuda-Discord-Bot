#Importing stuff
import nextcord, datetime, asyncio, time, random, csv
from nextcord import SlashOption, Interaction, User, ChannelType, Intents
from nextcord.abc import GuildChannel
from nextcord.ext import commands
token = open("token.txt").read()
serverID = 1042558127272370257

#Setting message content intent to true
intents = Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='?', intents=intents)


@client.slash_command(name="ping", description="simple ping", guild_ids=[serverID])
async def ping(interaction: Interaction):
    await interaction.response.send_message("Pong! :ping_pong:")

@client.event
async def on_ready():
    print(f"Logged in as: {client.user.name}")
    await client.change_presence(activity=nextcord.Activity(type = nextcord.ActivityType.watching, name = "Leon's YouTube Channel"))

if __name__ == '__main__':
    client.run(token)