import discord
from discord.ext import commands
import os

# إعداد الصلاحيات
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

CHANNEL_ID = 1381313175850901505

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        try:
            await channel.connect()
            print("Successfully connected to the voice channel!")
        except Exception as e:
            print(f"Failed to connect: {e}")
    else:
        print("Voice channel not found.")

bot.run('MTU1OTQyODMyMjIyNjczMzE4OA.G-n_0m.sfQRCjsofPaDz2QniWt102JtkolNBaaxWa2jwU')
