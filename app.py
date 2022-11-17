#Importing stuff
import nextcord, datetime, asyncio, time, random, csv
from nextcord import SlashOption, Interaction, User, ChannelType, Intents
from nextcord.abc import GuildChannel
from nextcord.ext import commands
token = open("token.txt").read()
test = open("serverID.txt").read()
serverID = 1042558127272370257

#Setting message content intent to true
intents = Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='?', intents=intents)

#Simple ping command
@client.slash_command(name="ping", description="simple ping", guild_ids=[serverID])
async def ping(interaction: Interaction):
    await interaction.response.send_message("Pong! :ping_pong:")

#Morning schedule message
async def schedule_daily_message():
    while True:
        now = datetime.datetime.now()
        then = now.replace(hour=9, minute=00)
        if then < now:
            then += datetime.timedelta(days=1)
        wait_time = (then-now).total_seconds()
        await asyncio.sleep(wait_time)

        channel = client.get_channel(1042563148928012439)

        await channel.send("Good morning!")
        time.sleep(60) #1 min buffer due to bot spamming channel
        await asyncio.sleep(1)

#When bot first runs
@client.event
async def on_ready():
    print(f"Logged in as: {client.user.name}")
    await client.change_presence(activity=nextcord.Activity(type = nextcord.ActivityType.watching, name = "Leon's YouTube Channel"))
    await schedule_daily_message()
    
if __name__ == '__main__':
    client.run(token)