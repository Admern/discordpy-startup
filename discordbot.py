from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

CHANNEL_ID = 802142210581594123

# 任意のチャンネルで挨拶する非同期関数を定義
async def greet():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('turn on')

# bot起動時に実行されるイベントハンドラを定義
@bot.event
async def on_ready():
    await greet() # 挨拶する非同期関数を実行

bot.run(token)
