import discord
from discord.ext import commands
import os

# إعداد الصلاحيات
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# آيدي الروم الصوتي
VOICE_CHANNEL_ID = 1381313175850901505

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    try:
        channel = bot.get_channel(VOICE_CHANNEL_ID)
        if channel and isinstance(channel, discord.VoiceChannel):
            await channel.connect()
            print(f"Connected to voice channel: {channel.name}")
        else:
            print("لم يتم العثور على الروم الصوتي، تأكد من الـ ID.")
    except Exception as e:
        print(f"خطأ أثناء الاتصال بالروم: {e}")

# توكن البوت
BOT_TOKEN = "MTU1OTQyODMyMjIyNjczMzE4OA.GCDNqB.938QsZ1awe0i1-pB_Qulwy8FdLLjBHEUIJXZAA"

bot.run(BOT_TOKEN)
