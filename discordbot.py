from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

CHANNEL_ID = 802142210581594123

# 任意のチャンネルで挨拶する非同期関数を定義
async def greet():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send('turn on')

# bot起動時に実行されるイベントハンドラを定義
@bot.event
async def on_ready():
    await greet() # 挨拶する非同期関数を実行

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

# 返信する非同期関数を定義
async def reply(message):
    reply = f'{message.author.mention} reminder' # 返信メッセージの作成
    await message.channel.send(reply) # 返信メッセージを送信

# 発言時に実行されるイベントハンドラを定義
@bot.event
async def on_message(message):
    if bot.user in message.mentions: # 話しかけられたかの判定
        await reply(message) # 返信する非同期関数を実行

bot.run(token)
