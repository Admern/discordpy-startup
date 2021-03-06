from discord.ext import commands
import os
import traceback
import asyncio

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

CHANNEL_ID = 802142210581594123

# 任意のチャンネルで挨拶する非同期関数を定義
#async def greet():
#    channel = bot.get_channel(CHANNEL_ID)
#    await channel.send('turn on')

# 返信する非同期関数を定義
async def reply(message):
    reply = f'{message.author.mention}\nyour id is {message.id}' # 返信メッセージの作成
    await message.channel.send(reply) # 返信メッセージを送信


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.event
# bot起動時に実行されるイベントハンドラを定義
async def on_ready():
    await greet() 

@bot.event
# 挨拶する非同期関数を実行
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.event
# 発言時に実行されるイベントハンドラを定義
async def on_message(message):
    if message.channel.id == CHANNEL_ID:
#        if message.content.startswith('$greet'):
#            channel = message.channel
#            await channel.send('Say hello!')
#
#            def check(m):
#                return m.content == 'hello' and m.channel == channel
#
#            msg = await client.wait_for('message', check=check)
#            await channel.send('Hello {.author}!'.format(msg))

        if message.content == "/ignore":
            ignoreMessageChannel = message.channel
            
            await message.channel.send(f"`削除しないメッセージを記述してください`")
            def ignoreMessageCheck(m):
                return m.channel == ignoreMessageChannel 
            msg = await client.wait_for("message", check=ignoreMessageCheck)
            await message.channel.send("削除対象から除外しました")
        
        if bot.user in message.mentions: #話しかけられたかの判定
            await reply(message) # 返信する非同期関数を実行
            return
        if message.author.bot:
            return
#        if message.content == "delete":
#        await message.channel.send("delete a message after 5mins")
        await asyncio.sleep(10)
        await message.delete()
        return
            
#        if message.content == "test":
#            await message.channel.send(f'{message.channel}') #チャンネルID送信
#            return
#        await message.channel.send("received a message")


bot.run(token)
