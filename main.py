import discord
from discord.ext import commands

# 設定機器人的意圖 (Intents)
intents = discord.Intents.default()
intents.message_content = True

# 初始化機器人，設定指令前綴為 '>'
bot = commands.Bot(command_prefix='>', intents=intents)

# 當輸入 >ping 時，機器人會回應 pong
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

# 啟動機器人（請將下方文字替換成您的最新 Token）
bot.run('MTU1NjE3OTMwMzIwMzM0ODUwMQ.GFqpzO.7YodpCbXD8kfngvZ5wMNL5H5xdSnVZwWjBY_ls')
