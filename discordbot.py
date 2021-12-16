import discord
import datetime

TOKEN = 'Nzg2ODMyMDE5NDA0NjE5Nzg3.X9MIbA.DK9m79H5SCieNxFCg3lF95JhKFE'

client = discord.Client()

@client.event
async def on_ready():
    #起動時の通知
    print("ログインしました。")

@client.event
async def on_message(message):
    #現在時刻を取得する
    if message.content == '/now':
        now = datetime.datetime.now()
        await message.channel.send(now)
    if message.content == '/nyan':
        await message.channel.send("にゃーん")

    if message .content == '/lol':
        await message.channel.send("あははははははははは")
client.run(TOKEN)